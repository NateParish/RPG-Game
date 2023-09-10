import pygame
import variables
imageSize = variables.heroSize

playerWalkingRightImages = []
playerWalkingLeftImages = []
playerWalkingUpImages = []
playerWalkingDownImages = []



class Spritesheet:
    def __init__(self,fileName):
        self.fileName = fileName
        self.sprite_sheet = pygame.image.load(fileName).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite


def loadSprites(spriteSheet, spriteX, spriteY, spriteHeight, spriteWidth, images, imgCount):

    imageNum = 0

    while imageNum < imgCount:
        images.append(pygame.transform.scale(spriteSheet.get_sprite(spriteX,spriteY,spriteHeight,spriteWidth),imageSize))
        imageNum +=1
        spriteX = spriteX + spriteWidth


heroSpriteSheet = Spritesheet(variables.heroSpriteSheetPath)

loadSprites(heroSpriteSheet,0,704,64,64,playerWalkingRightImages,9)
loadSprites(heroSpriteSheet,0,576,64,64,playerWalkingLeftImages,9)
loadSprites(heroSpriteSheet,0,512,64,64,playerWalkingUpImages,9)
loadSprites(heroSpriteSheet,0,640,64,64,playerWalkingDownImages,9)
