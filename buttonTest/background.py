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
import sys, pygame, os
from pygame.locals import *

class Background:
    
    # Draws itself on the entire screen, replaces everything already there
    def draw(self):
        self.screen.blit(self.boardBackgroundSurface, (0,0))

    
    def __init__(self):
        self.screen = pygame.display.get_surface()
        
        # prepare the background
        boardBackgroundName = os.path.join("basicButtons.png")
        self.boardBackgroundSurface = pygame.image.load(boardBackgroundName)

        self.draw()
        pygame.display.flip()

    # Updates the given area of the screen
    def repair(self, cleanCoord):
        area = Rect(cleanCoord[0], cleanCoord[1], 40, 40)
        self.screen.blit(self.boardBackgroundSurface, cleanCoord, area)
        
