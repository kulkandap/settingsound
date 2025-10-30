# Magic Type

import pygame
import main_menu
import score
import character
import background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080)) # Game resolution 1920 pixel times 1080 pixels
clock = pygame.time.Clock()
title = pygame.display.set_caption("Magic Type")
running = True
dt = 0

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill background with a fhd picture 
    screen.fill((0, 0, 0))
    screen.blit(background.softmountain, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
