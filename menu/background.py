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
        self.screen.blit(self.backgroundSurface, (0,0))
    
    def __init__(self):
        self.screen = pygame.display.get_surface()
        
        # prepare the background
        backgroundName = os.path.join("menuBack.png")
        self.backgroundSurface = pygame.image.load(backgroundName)

        self.draw()
        pygame.display.flip()

    # Repairs the background in the area used by the menu. This area will always
    # be considered dirty in an update of the screen, since it always is altered
    # by the menu
    def repair(self):
        # top left x = 125 Y = 45
        # bottom right x = 324 y = 394
        progListRect = Rect(125, 45, 199, 349)
        self.screen.blit(self.backgroundSurface, (125, 45), progListRect)
        progPropRect = Rect(365, 34, 244, 424)
        self.screen.blit(self.backgroundSurface, (365, 34), progPropRect)
    
    def blackout(self):
        self.screen.fill(color.Color("black"))
        
        