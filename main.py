import sys, random, pygame

def main():

    red = pygame.Color(255, 0, 0)
    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)

    pygame.init()
    pygame.display.set_caption("Snake Game for 2 Players")
    screen = pygame.display.set_mode((720, 480))

    numberOfPlayers = -1

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

        for i in range(numberOfPlayers):
            

        pygame.display.flip()

main()