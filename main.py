import sys, random, pygame
from snake import *


def main():

    red = pygame.Color(255, 0, 0)
    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    green = pygame.Color(0, 255, 255)
    orange = pygame.Color(255, 255, 0)

    pygame.init()
    pygame.display.set_caption("Snake Game for 2 Players")
    screen = pygame.display.set_mode((720, 480))

    numberOfPlayers = -1
    direction1 ='RIGHT'

    while numberOfPlayers == -1:
        screen.fill(white)

        font = pygame.font.SysFont('calibri', 48)
        surface = font.render('Press 1 for 1 player!', True, black)
        surface2 = font.render('Press 2 for 2 players!', True, black)
        rect = surface.get_rect()
        rect2 = surface2.get_rect()
        rect.midtop = (360, 120)
        rect2.midtop = (360, 240)
        screen.blit(surface, rect)
        screen.blit(surface2, rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    numberOfPlayers = 1
                if event.key == pygame.K_2:
                    numberOfPlayers = 2

        if numberOfPlayers == 1:
            snake1 = Snake(100, 50, 90, 50)
        else:
            snake1 = Snake(100, 50, 90, 50)
            snake2 = Snake(380, 50, 390, 50)
            direction2 = 'LEFT'

        pygame.display.flip()





main()