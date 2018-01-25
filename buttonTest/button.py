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


class Button:
    
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.screen = pygame.display.get_surface()
        
        dotName = os.path.join("dot.png")
        self.dotSurface = pygame.image.load(dotName)
        
    def toString(self):
        return self.name
    
    def down(self):
        # print "down - " + self.name
        self.screen.blit(self.dotSurface, self.pos)
        
    def up(self):
        # print "up - " + self.name
        self.background.repair(self.pos)



