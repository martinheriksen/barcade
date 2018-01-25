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
import sys, pygame, button
from pygame.locals import *
from button import *
from background import *

pygame.init()

# window = pygame.display.set_mode((640, 480), FULLSCREEN)
window = pygame.display.set_mode((640, 480))

background = Background()

Button.background = background

# Still need to add the start button
# Start button has the following coordinates = (99,219)
buttons = {306 : Button("P1 - B1 - Key ' '", (239,  39)),
           308 : Button("P1 - B2 - Key ' '", (299,  39)),
           32  : Button("P1 - B3 - Key ' '", (359,  39)),
           304 : Button("P1 - B4 - Key ' '", (239,  99)),
           122 : Button("P1 - B5 - Key 'z'", (299,  99)),
           120 : Button("P1 - B6 - Key 'x'", (359,  99)),
#            99  : Button("P1 - B7 - Key 'c'"),
#            53  : Button("P1 - B8 - Key '5'"),
           264 : Button("P1 - JU - Key ' '", (119,  40)),
           260 : Button("P1 - JL - Key ' '", ( 80,  80)),
           262 : Button("P1 - JR - Key ' '", (158,  80)),
           258 : Button("P1 - JD - Key ' '", (119, 118)),
           
           51  : Button("Coin", (99,219)),
           49  : Button("1P - Key '1'", (259, 219)),
           50  : Button("2P - Key '2'", (439, 219)),
           
           97  : Button("P2 - B1 - Key 'a'", (239, 319)),
           115 : Button("P2 - B2 - Key 's'", (299, 319)),
           113 : Button("P2 - B3 - Key 'q'", (359, 319)),
           119 : Button("P2 - B4 - Key 'w'", (239, 379)),
           101 : Button("P2 - B5 - Key 'e'", (299, 379)),
           229 : Button("P2 - B6 - Key ' '", (359, 379)),
#            314 : Button("P2 - B7 - Key ' '"),
#            54  : Button("P2 - B8 - Key '6'"),
           114 : Button("P2 - JU - Key 'r'", (119, 320)),
           100 : Button("P2 - JL - Key 'd'", ( 80, 360)),
           103 : Button("P2 - JR - Key 'g'", (158, 360)),
           102 : Button("P2 - JD - Key 'f'", (119, 398))}

countState = 0

programRunning = True

while programRunning:
    event = pygame.event.wait()
    
    if event.type == KEYDOWN:
        if event.key == 27:
            sys.exit(0)
        if buttons.__contains__(event.key):
            buttons[event.key].down()
        if event.key == 51 or event.key == 49:
            countState = countState + 1
            
            if countState == 2:
                programRunning = False
	
        
    if event.type == KEYUP:
        if buttons.__contains__(event.key):
            buttons[event.key].up()
        if event.key == 51 or event.key == 49:
            countState = countState + 1
    
    pygame.display.flip()