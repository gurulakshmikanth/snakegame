import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# display size
display_width = 600
display_height = 400

dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

snake_block = 10  # size of snake
snake_speed = 15  # speed of snake

font_style = pygame.font.SysFont('impact', 25)
score_font = pygame.font.SysFont('impact', 20)


def Your_score(score):
    value = score_font.render('Score: ' + str(score), True, black)
    dis.blit(value, [0, 0])  # used to draw or create the changes


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [display_width / 6, display_height / 3])


def gameloop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # generate the food randomly
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            lost = 'You Lost Press C to Play Again or Q to Quit'
            message(lost, red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # condition for either run or exit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        # increasing the snake size
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1,y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:  # one is removed
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameloop()
