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
import os, pygame, threading, json
from pygame.locals import *

from background import *
from menuList import *
from emulator import Emulator

# Load settings
settingsFile = open('../data/settings.json')
settingsData = json.loads(settingsFile.read())
Emulator.settings = settingsData


pygame.init()

pygame.mouse.set_visible(False)

size = width, height =  640, 480
# window = pygame.display.set_mode(size, FULLSCREEN)
window = pygame.display.set_mode((640, 480))

background = Background()

menuList = MenuList(background)


background.draw()

menuList.draw()

pygame.display.flip()

# Create the screensaver

background.blackoutBool = False
def blackout():
    background.blackoutBool = True
    background.blackout()
    pygame.display.flip()

t = threading.Timer(settingsData['screensaver']['timer'], blackout)
t.start()

comboState = 0

while True:
    # reset screensaver
    t.cancel()
    if background.blackoutBool == True:
        background.draw()
        menuList.programPointer.drawCurrent()
        pygame.display.flip()
        background.blackoutBool = False
    t = threading.Timer(settingsData['screensaver']['timer'], blackout)
    t.start()
    
    event = pygame.event.wait()
    
    if event.type == KEYDOWN:
        if event.key == 27:
            sys.exit(0)
        if event.key == 274 or event.key == 258:
            menuList.moveUp()
            pygame.display.flip()
        if event.key == 273 or event.key == 264:
            menuList.moveDown()
            pygame.display.flip()
        if event.key == 13 or event.key == 306:
            menuList.select()
            pygame.display.flip()
        if event.key == 50 or event.key == 51:
            comboState = comboState + 1
            if comboState == 2:
                # Since both buttons are pressed down at the same time
                # we can start the diagnostic program
                pygame.display.set_mode((size))
                pygame.display.update()
                os.system("/home/mhe/Programming/itu/buttonTest/start")
                pygame.display.set_mode((size),FULLSCREEN)
                background.draw()
                menuList.programPointer.drawCurrent()
                pygame.display.flip()
                
    if event.type == KEYUP:
        if event.key == 50 or event.key == 51:
            comboState = comboState - 1
    
