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
import os, pygame
from pygame.locals import *

from background import *
from program import *

class MenuList:
    
    
    def draw(self):
        self.programPointer.drawCurrent()
    
    # Moves the select pointer up the list, and updates the graphics
    def moveUp(self):
        self.background.repair()
        self.programPointer = self.programPointer.nextProgram
        self.programPointer.drawCurrent()
        # self.programPointer.drawMoveDown(self.background)
        
    # Moves the select pointer down the list, and updates the graphics
    def moveDown(self):
        self.background.repair()
        self.programPointer = self.programPointer.prevProgram
        self.programPointer.drawCurrent()
        
        
    # A game is selected, and the respective game is started.
    def select(self):
        self.programPointer.execute()
        self.background.draw()
        self.programPointer.drawCurrent()
    
    def loadProgramList(self):
        tempProgramPointer = Program("Airwolf", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen airwolf", None, "airwolf.png", "The Airwolf arcade game by \nKyugo Boueki. Fly around \nin your supersonic military \nhelicopter, undertaking \nvarious missions.")
        firstProgramPointer = tempProgramPointer
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Altered Beast", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen altbeast", self.programPointer, "altbeast.png", "Altered Beast is a platform/\nfighting game that puts the \nplayer in control of a \ncenturion who had died in \nbattle. The centurion has \nbeen raised from the dead to \nrescue Zeus' daughter.")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Asterix", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen -hs 2 -ws 2 asterix", self.programPointer, "asterix.png", "Asterix is a \nhorizontal-scrolling beat'em \nup arcade game released in \n1992 by Konami.")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Bowl-O-Rama", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen bowlrama", self.programPointer, "bowlrama.png", "Classic bowling \ncombined with some nice \ntunes.")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Bubble Bobble", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen -hs 2 -ws 2 bublbobl", self.programPointer, "bublbobl.png", "No introduction should be \nnecessary for this game! \nIf you do not know this game, \nthen please step away from \nthe machine.")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Contra", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen contra", self.programPointer, "contra.png")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Ecofighters", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen ecofghtr", self.programPointer, "ecofghtr.png")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Golden Axe", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen -hs 2 -ws 2 goldnaxe", self.programPointer, "goldnaxe.png")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Space Invaders", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen -hs 2 -ws 2 invaders", self.programPointer, "invaders.png")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Street Fighter", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen sf", self.programPointer, "sf.png")
        self.programPointer = tempProgramPointer
        
        tempProgramPointer = Program("Street Fighter II", "/usr/games/xmame", "xmame -ctrlr xarcade -fullscreen sf2", self.programPointer, "sf2.png")
        self.programPointer = tempProgramPointer
        
        self.programPointer = firstProgramPointer
        self.programPointer.prevProgram = tempProgramPointer
        tempProgramPointer.nextProgram = firstProgramPointer
        
    def __init__(self, background):
        self.background = background
        self.loadProgramList()
