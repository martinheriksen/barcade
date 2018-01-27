"""
This file is part of Barcade.

Barcade is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Barcade is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Barcade.  If not, see <http://www.gnu.org/licenses/>.
"""
import os, pygame, json
from pygame.locals import *

from background import *
from program import *

class MenuList:
    
    
    def draw(self):
        if self.emptyList == True:
            return

        self.programPointer.drawCurrent()
    
    # Moves the select pointer up the list, and updates the graphics
    def moveUp(self):
        if self.emptyList == True:
            return

        self.background.repair()
        self.programPointer = self.programPointer.nextProgram
        self.programPointer.drawCurrent()
        # self.programPointer.drawMoveDown(self.background)
        
    # Moves the select pointer down the list, and updates the graphics
    def moveDown(self):
        if self.emptyList == True:
            return

        self.background.repair()
        self.programPointer = self.programPointer.prevProgram
        self.programPointer.drawCurrent()
        
        
    # A game is selected, and the respective game is started.
    def select(self):
        if self.emptyList == True:
            return

        self.programPointer.execute()
        self.background.draw()
        self.programPointer.drawCurrent()
    
    def loadProgramList(self):
        self.emptyList = True
        self.programPointer  = None

        # rootdir = '../programs/'

        for subdir, dirs, files in os.walk('../data/programs/'):
            programFileExists = False
            screenshotFileExists = False

            for file in files:
                if file == "readme":
                    continue

                if file == "program.json":
                    print os.path.join(subdir, file)
                    programFile = open(os.path.join(subdir, file))
                    programData = json.loads(programFile.read())

                    if programData['enabled'] == False:
                        continue

                    programFileExists = True

                if file == "screenshot.png":
                    screenshotFilePath = os.path.join(subdir, file)
                    screenshotFileExists = True

            if programFileExists == True and screenshotFileExists == True:
                print "Creating entry"
                tempProgramPointer = Program(programData["title"], programData["emulator"], programData["emulator_argument"], self.programPointer, screenshotFilePath, programData["description"])
                self.programPointer = tempProgramPointer

                if self.emptyList == True:
                    firstProgramPointer = tempProgramPointer
                    self.emptyList = False

        if self.emptyList == False:
            self.programPointer = firstProgramPointer
            self.programPointer.prevProgram = tempProgramPointer
            tempProgramPointer.nextProgram = firstProgramPointer
        
    def __init__(self, background):
        self.background = background
        self.loadProgramList()
