
import pygame
import variables


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


class Hero:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.img = image
        self.mask = pygame.mask.from_surface(self.img)

    def updateImage(self, image):
        self.img = image

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, xVel, yVel):
        self.x += xVel
        self.y += yVel

    def off_screen(self, width):
        return not(self.x <= width  and self.x >= 0)

    def collision(self, obj):
        return collide(self, obj)

