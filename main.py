import sys, random, pygame, time
from snake import *

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 255)
orange = pygame.Color(255, 255, 0)
blue = pygame.Color(0, 0, 255)

def gameOver(string, screen):

    font = pygame.font.SysFont('calibri', 56)
    surface = font.render('Game Over!' + string, True, red)
    rect = surface.get_rect()
    rect.midtop = (360, 45)
    screen.blit(surface, rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()


def showScore(screen, score1, score2, isGameOver = False):

    fontSize = 18 if not isGameOver else 40
    font = pygame.font.SysFont('calibri', fontSize)
    surface = font.render('Player 1 Score: ' + str(score1), True, black)
    surface2 = font.render('Player 2 Score: ' + str(score2), True, black)
    rect = surface.get_rect()
    rect2 = surface2.get_rect()

    xValue = 360 if isGameOver else 75
    yValue = 130 if isGameOver else 25
    x2Value = 360 if isGameOver else 75
    y2Value = 190 if isGameOver else 50

    rect.midtop = (xValue, yValue)
    rect2.midtop = (x2Value, y2Value)
    screen.blit(surface, rect)
    screen.blit(surface2, rect2)



def main():

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
            snake2 = Snake(400, 430, 410, 430, 420, 430)
            direction2 = 'LEFT'

        pygame.display.flip()


    while snake1.inBounds() and snake2.inBounds():

        screen.fill(white)
        showScore(screen, snake1.score, snake2.score)

        snake1.body.insert(0, list(snake1.position))
        snake1.update(direction1)

        if numberOfPlayers == 2:

            if snake2.position[0] == foodPosition[0] and snake2.position[1] == foodPosition[1]:
                snake2.score += 1
                foodSpawned = False
            else:
                snake2.body.pop()

            snake2.body.insert(0, list(snake2.position))
            snake2.update(direction2)

        if not snake1.inBounds():
            gameOver("Player 2 wins!", screen)


        if not snake2.inBounds():
            gameOver("Player 1 wins!", screen)


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

        if not foodSpawned:
            foodPosition = [random.randrange(0, 72) * 10, random.randrange(0, 48) * 10]
            foodSpawned = True

        pygame.draw.rect(screen, blue, pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

        if snake1.position[0] == foodPosition[0] and snake1.position[1] == foodPosition[1]:
            snake1.score += 1
            foodSpawned = False
        else:
            snake1.body.pop()


        for body1 in snake1.body:
            pygame.draw.rect(screen, green, pygame.Rect(body1[0], body1[1], 10, 10))

        if numberOfPlayers == 2:
            if snake2.position[0] == foodPosition[0] and snake2.position[1] == foodPosition[1]:
                snake2.score += 1
                foodSpawned = False
            else:
                snake1.body.pop()

            for body2 in snake2.body:
                pygame.draw.rect(screen, orange, pygame.Rect(body2[0], body2[1], 10, 10))


        fpsController.tick(20)
        pygame.display.flip()


main()