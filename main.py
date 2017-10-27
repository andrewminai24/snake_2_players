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
    fpsController = pygame.time.Clock()

    numberOfPlayers = -1
    direction1 ='RIGHT'

    foodPosition = [random.randrange(0, 72) * 10, random.randrange(0, 48) * 10]
    foodSpawned = True

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
            snake1 = Snake(100, 50, 90, 50, 80, 50)
        else:
            snake1 = Snake(100, 50, 90, 50, 80, 50)
            snake2 = Snake(380, 50, 390, 50, 400, 50)
            direction2 = 'LEFT'

        pygame.display.flip()


    while snake1.inBounds() and snake2.inBounds():

        screen.fill(white)

        snake1.body.insert(0, list(snake1.position))
        snake2.body.insert(0, list(snake2.position))
        snake1.update(direction1)
        snake2.update(direction2)

        if not snake1.inBounds():
            # gameOver("Player 2 wins!")
            continue        # change

        if not snake2.inBounds():
            # gameOver("Player 1 wins!")
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction2 != 'RIGHT':
                    direction2 = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction2 != 'LEFT':
                    direction2 = 'RIGHT'
                elif event.key == pygame.K_UP and direction2 != 'DOWN':
                    direction2 = 'UP'
                elif event.key == pygame.K_DOWN and direction2 != 'UP':
                    direction2 = 'DOWN'
                elif event.key == pygame.K_a and direction1 != 'RIGHT':
                    direction1 = 'LEFT'
                elif event.key == pygame.K_d and direction1 != 'LEFT':
                    direction1 = 'RIGHT'
                elif event.key == pygame.K_s and direction1 != 'UP':
                    direction1 = 'DOWN'
                elif event.key == pygame.K_w and direction1 != 'DOWN':
                    direction1 = 'UP'

        if snake1.position[0] == foodPosition[0] and snake1.position[1] == foodPosition[1]:
            snake1.score += 1
            foodSpawned = False
        else:
            snake1.body.pop()

        if snake2.position[0] == foodPosition[0] and snake2.position[1] == foodPosition[1]:
            snake2.score += 1
            foodSpawned = False
        else:
            snake2.body.pop()

        if not foodSpawned:
            foodPosition = [random.randrange(0, 72) * 10, random.randrange(0, 48) * 10]
            foodSpawned = True

        for body1 in snake1.body:
            pygame.draw.rect(screen, green, pygame.Rect(body1[0], body1[1], 10, 10))

        if not numberOfPlayers:
            for body2 in snake2.body:
                pygame.draw.rect(screen, orange, pygame.Rect(body2[0], body2[1], 10, 10))


        fpsController.tick(20)
        pygame.display.flip()


main()