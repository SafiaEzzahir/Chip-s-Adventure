import pygame, sys
from pygame.locals import *

print("\n hi i'm the layout generator\n")

wid = int(input("\n how wide is ur screen\n\n "))
leg = int(input("\n and how long is it ( ͡ಥ ͜ʖ ͡ಥ)\n\n "))

pygame.init()

screen = pygame.display.set_mode((wid, leg))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    pygame.display.update()