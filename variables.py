import pygame
import os


pygame.font.init()



SCREENWIDTH = 1500
SCREENHEIGHT = 750
FPS = 60
playerVel = 3
heroSize = (175, 175)
heroStartX = 100
heroStartY = 100

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

heroSpriteSheetPath = 'images/player sprite sheet.png'


mainFont = pygame.font.SysFont("ariel", 50)
lostFont = pygame.font.SysFont("ariel", 60)
titleFont = pygame.font.SysFont("ariel", 50)


WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
CAPTION = "Title of Game"


