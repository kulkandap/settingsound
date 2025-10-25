import pygame

# https://www.peppercarrot.com/0_sources/0ther/wallpapers/hi-res/2017-04-10_Only-Komona_by-David-Revoy.jpg
bg = pygame.image.load("2017-04-10_Only-Komona_by-David-Revoy.jpg")
def backgroundImg(bg):
    size = pygame.transform.scale(bg, (1920, 1080))
    screen.blit(size, (0, 0))
