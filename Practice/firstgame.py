import pygame, sys
from pygame.locals import *

#setup the game
pygame.init()

#setup window
windowFrame = pygame.display.set_mode((500,400), 0, 32)

#setup windoW caption
pygame.display.set_caption("Hello World")

#setup colour

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
TEAL = (0, 128, 128)

#setup the font
basicFont = pygame.font.SysFont(None, 48)

#setup the text
text = basicFont.render("HELLO WORLD", True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowFrame.get_rect().centerx
textRect.centery = windowFrame.get_rect().centery

#Paint the window background
windowFrame.fill(TEAL)

#setup window caption

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowFrame)
pixArray[480][380] = BLACK
del pixArray
#setup window caption

# draw the text onto the surface
windowFrame.blit(text, textRect)


# draw the window onto the screen
pygame.display.update()


#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

