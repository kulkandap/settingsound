import pygame

valley = pygame.image.load("tux.jpg")
def backgroundImg(valley):
    size = pygame.transform.scale(valley, (1920, 1080))
    screen.blit(size, (0, 0))
