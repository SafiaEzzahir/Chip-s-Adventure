import math
import pygame

class ControllablePoint():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = False
        self.dragging= False

    def display(self, ds):
        pygame.draw.circle(ds, self.color, (self.x, self.y), 3, width=1)

    def drag(self, x, y):
        val = (self.x-x)**2+ (self.y-y)**2
        if math.sqrt(val) <=3:
            self.dragging = True

    def drop(self, x, y):
        self.dragging = False
     
    def move(self, x, y):
        if(self.dragging):
            self.x = x
            self.y = y
               
    def do(self):
        None
