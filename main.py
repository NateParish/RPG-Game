import pygame
import os
import time
import random
import hero
import variables
import spritesheet


pygame.font.init()
WIN = pygame.display.set_mode((variables.SCREENWIDTH, variables.SCREENHEIGHT))

pygame.display.set_caption(variables.CAPTION)
index = 0


def main():
    run = True
    FPS = variables.FPS
    mainFont = variables.mainFont
    lostFont = variables.lostFont
    index = 0
    delay = 0

    clock = pygame.time.Clock()


    lost = False


    playerImage = spritesheet.playerWalkingRightImages[index]

    player1 = hero.Hero(variables.heroStartX, variables.heroStartY, playerImage)


    def redraw_window():
        WIN.fill(variables.BLACK)
        player1.draw(WIN)
        pygame.display.update()

    while run:

        clock.tick(FPS)
                        
        redraw_window()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # left
            player1.move(variables.playerVel * -1, 0)
            delay +=1
            if delay > 2:
                index = (index + 1)% len(spritesheet.playerWalkingLeftImages)
                player1.updateImage(spritesheet.playerWalkingLeftImages[index])
                delay = 0

        if keys[pygame.K_RIGHT]: # left
            player1.move(variables.playerVel, 0)
            delay +=1
            if delay > 2:
                index = (index + 1)% len(spritesheet.playerWalkingRightImages)
                player1.updateImage(spritesheet.playerWalkingRightImages[index])
                delay = 0

        if keys[pygame.K_UP]: # left
            player1.move(0, variables.playerVel * -1)
            delay +=1
            if delay > 2:
                index = (index + 1)% len(spritesheet.playerWalkingUpImages)
                player1.updateImage(spritesheet.playerWalkingUpImages[index])
                delay = 0

        if keys[pygame.K_DOWN]: # left
            player1.move(0, variables.playerVel)
            delay +=1
            if delay > 2:
                index = (index + 1)% len(spritesheet.playerWalkingDownImages)
                player1.updateImage(spritesheet.playerWalkingDownImages[index])
                delay = 0

        if keys[pygame.K_SPACE]:
            delay +=1
            if delay > 3:
                index = (index + 1)% len(spritesheet.playerWalkingLeftImages)
                player1.updateImage(spritesheet.playerWalkingLeftImages[index])
                delay = 0





def main_menu():
    
    run = True

    while run:

        WIN.fill(variables.BLACK)
        titleLabel = variables.titleFont.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(titleLabel, (variables.SCREENWIDTH/2 - titleLabel.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()



