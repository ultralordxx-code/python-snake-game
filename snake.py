import pygame
import random

pygame.init()

# Screen
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255,255,255)
green = (0,200,0)
red = (200,0,0)
black = (0,0,0)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font = pygame.font.SysFont(None, 35)

def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])

def message(msg,color):
    text = font.render(msg, True, color)
    screen.blit(text,[width/6,height/3])

def game():
    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    foodx = random.randrange(0,width-snake_block,10)
    foody = random.randrange(0,height-snake_block,10)

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = random.randrange(0,width-snake_block,10)
            foody = random.randrange(0,height-snake_block,10)
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game()