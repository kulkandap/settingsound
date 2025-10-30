import pygame

pygame.init()

pygame.display.set_caption("Magic Type")

white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

screen = pygame.display.set_mode((600,600))
screen.fill(black)
pygame.draw.rect(screen,white,(200, 180, 200, 75))
pygame.draw.rect(screen,white,(200, 280, 200, 75))
pygame.draw.rect(screen,white,(200, 380, 200, 75))

sys_font = pygame.font.SysFont("menlo",55)
sys_fontplay = pygame.font.SysFont("menlo",40)
message_play = sys_font.render("Play",True,green)
message_setting = sys_font.render("Setting",True,green)
message_quit = sys_font.render("Quit",True,green)
screen.blit(message_play, (220,200))
screen.blit(message_setting, (220, 300))
screen.blit(message_quit, (220, 400))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.flip()
    pygame.display.update()
pygame.quit()  
