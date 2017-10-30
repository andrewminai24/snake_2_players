"""
    In this game, the controllers for player 1 is A W S D keys. A for left, W for up, S for down, and D for right.
    If 2 players are playing, the player 2 moves by the UP DOWN LEFT RIGHT keys.
"""

import sys, random, pygame, time
from snake import *

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 255)
orange = pygame.Color(255, 255, 0)
blue = pygame.Color(0, 0, 255)

def gameOver(screen, string = ""):
    font = pygame.font.SysFont('calibri', 56)
    surface = font.render('Game Over! ' + string, True, red)
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
    screen = pygame.display.set_mode((720, 480))       # or 1200, 700 also will work
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
            snake1 = Snake(100, 90, 90, 90, 80, 90)
        else:
            snake1 = Snake(100, 90, 90, 90, 80, 90)
            snake2 = Snake(400, 390, 410, 390, 420, 390)
            direction2 = 'LEFT'

        pygame.display.flip()


    while snake1.inBounds() and snake2.inBounds():
        screen.fill(white)
        showScore(screen, snake1.score, snake2.score)

        snake1.body.insert(0, list(snake1.position))
        snake1.update(direction1)

        # checking if player 1 ate the food, if yes then make the snake longer
        if snake1.position[0] == foodPosition[0] and snake1.position[1] == foodPosition[1]:
            snake1.score += 1
            foodSpawned = False
        else:
            snake1.body.pop()

        if numberOfPlayers == 2:
            # checking if player 2 ate the food, if there's 2 players playing
            if snake2.position[0] == foodPosition[0] and snake2.position[1] == foodPosition[1]:
                snake2.score += 1
                foodSpawned = False
            else:
                snake2.body.pop()

            # updating the player 2's position
            snake2.body.insert(0, list(snake2.position))
            snake2.update(direction2)

        if not snake1.inBounds() and numberOfPlayers == 2:
            gameOver(screen, "Player 2 wins!")
            showScore(screen, snake1.score, snake2.score, True)

        if not snake1.inBounds() and numberOfPlayers == 1:
            gameOver(screen)
            showScore(screen, snake1.score, snake2.score, True)

        if not snake2.inBounds() and numberOfPlayers == 2:
            gameOver(screen, "Player 1 wins!")
            showScore(screen, snake1.score, snake2.score, True)


        for event in pygame.event.get():

            if event.type == pygame.QUIT or event.key == pygame.K_ESCAPE:
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

        # spawning the food, if there isn't any
        if not foodSpawned:
            foodPosition = [random.randrange(0, 72) * 10, random.randrange(0, 48) * 10]
            foodSpawned = True

        pygame.draw.rect(screen, blue, pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

        # drawing the player 1
        for body1 in snake1.body:
            # if the player 2 hits the player 1's body, then player 1 wins
            if snake2.position[0] == body1[0] and snake2.position[1] == body1[1]:
                gameOver(screen, "Player 1 wins!")

            pygame.draw.rect(screen, green, pygame.Rect(body1[0], body1[1], 10, 10))

        # if there's 2 players, drawing the second player
        if numberOfPlayers == 2:
            for body2 in snake2.body:
                # if the player 1 crashes into player 2's body, then player 1 loses
                if snake1.position[0] == body2[0] and snake1.position[1] == body2[1]:
                    gameOver(screen, "Player 2 wins!")

                pygame.draw.rect(screen, orange, pygame.Rect(body2[0], body2[1], 10, 10))

        # if the players crash by their heads, the winner is determined based on their scores
        if snake1.position[0] == snake2.position[0] and snake1.position[1] == snake2.position[1]:
            if snake1.score > snake2.score:
                gameOver(screen, "Player 1 wins!")
            elif snake1.score == snake2.score:
                gameOver(screen, "Tie!")
            else:
                gameOver(screen, "Player 2 wins!")

        fpsController.tick(20)
        pygame.display.flip()


main()
