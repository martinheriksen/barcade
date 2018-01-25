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
import sys, os, pygame
from pygame.locals import *
from pygame.font import *

# It also acts as a linked list, wher each element knows of the 
# previuos and next element in the list. That way is necessary only to
# hold a reference to the currently selected program, all references
# will still be intact. It is the builder of this lists responsibility
# to enshure that the list can become circular.
class Program:
    
    # I hardcoded all the menu coordinates, was much easier than doing it 
    # dynamically and there are only 7 coordinates
    prevCoord = [(135, 155),(135, 105),(135, 55)]
    currentCoord = (135, 205)
    nextCoord = [(135, 255),(135, 305),(135, 355)]
    
    def __init__(self, name, path, args, prevProgram, screenshot = None, text=None):
        self.name = name
        
        font = SysFont("Times New Roman", 30)
        self.nameCurrentSurface = font.render(name, True, (255,255,255))
        self.nameSurface = font.render(name, True, (155,155,155))
        self.path = path
        self.args = args.split(" ")
        if(prevProgram != None):
            self.prevProgram = prevProgram
            prevProgram.nextProgram = self
        
        self.screen = pygame.display.get_surface()
        
        # Prepare the screenshot
        if screenshot == None:
            screenshotName = os.path.join("noScreen.png")
            self.screenshot = pygame.image.load(screenshotName)
        else:
            screenshotName = os.path.join("screenshots", screenshot)
            self.screenshot = pygame.image.load(screenshotName)
        
        # prepare the text that describes the game
        if text != None:
            font = SysFont("Times New Roman", 25)
            self.text = pygame.Surface((244, 184))
            self.text.set_colorkey(Color("#000000"))
            splitText = text.split("\n")
            
            for n in range (0, len(splitText)):
                tempSurface = font.render(splitText[n], True, (255,255,255))
                self.text.blit(tempSurface, (0,25*n))
                if n >= 6:
                    break
        else:
            self.text = None
        
    
    def execute(self):
        # Using this instead of the os.system call, since if there is
        # an error in execution, os.system will halt the entire process.
        # Using os.spawn, the program is spawned in it's own process,
        # that does not take the menu process down, if there is an error.
        size = width, height =  640, 480
        pygame.display.set_mode((size))
        pygame.display.update()
        
        os.spawnv(os.P_WAIT, self.path, self.args)
        
        pygame.display.set_mode((size),FULLSCREEN)
        
        
    def renderText(self, dest):
        self.screen.blit(self.nameSurface, dest)
        
    def renderCurrentText(self, dest):
        self.screen.blit(self.nameCurrentSurface, dest)
        
    def drawPrev(self, counter, offset):
        if counter >= 3:
            return
        
        coord = (self.prevCoord[counter][0], self.prevCoord[counter][1] + offset)
        self.renderText(coord)
        self.prevProgram.drawPrev(counter + 1, offset)
        
    def drawNext(self, counter, offset):
        if counter >= 3:
            return
        coord = (self.nextCoord[counter][0], self.nextCoord[counter][1] + offset)
        self.renderText(coord)
        self.nextProgram.drawNext(counter + 1, offset)
        
    def drawMoveDown(self, background):
        offset = 20
        
        for i in range(1, 4):
            background.repair()
            offset = offset - 5
            coord = (self.currentCoord[0], self.currentCoord[1] + offset)
            self.renderText(coord)
            self.prevProgram.drawPrev(0, offset)
            self.nextProgram.drawNext(0, offset)
            pygame.display.flip()
    
    def drawCurrent(self):
        self.renderCurrentText(self.currentCoord)
        self.prevProgram.drawPrev(0, 0)
        self.nextProgram.drawNext(0, 0)
        self.drawInfo()
    
    def drawInfo(self):
        self.screen.blit(self.screenshot, (365,34))
        
        if self.text != None:
            self.screen.blit(self.text, (365,240))
