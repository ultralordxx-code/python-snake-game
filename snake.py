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

# Generate L blocks
num_blocks = 8
blocks = []

for i in range(num_blocks):
    x = random.randrange(0, width-30, 10)
    y = random.randrange(0, height-30, 10)
    blocks.append([x, y])


def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block, block])


# Draw L block
def draw_L_block(x, y):

    pygame.draw.rect(screen, red, [x, y, 10, 30])     # vertical part
    pygame.draw.rect(screen, red, [x, y+20, 30, 10])  # bottom part


def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width/6, height/3])


def gameLoop():

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width-10) / 10) * 10
    foody = round(random.randrange(0, height-10) / 10) * 10

    while not game_over:

        while game_close:

            screen.fill(black)
            message("Game Over! Q-Quit C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0

                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0


        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change

        screen.fill(black)

        pygame.draw.rect(screen, white, [foodx, foody, 10, 10])

        # draw L blocks
        for block in blocks:
            draw_L_block(block[0], block[1])


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)

        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]


        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True


        # block collision
        for bx, by in blocks:

            if (bx <= x1 <= bx+30 and by <= y1 <= by+30):
                game_close = True


        draw_snake(10, snake_List)

        pygame.display.update()


        if x1 == foodx and y1 == foody:

            foodx = round(random.randrange(0, width-10) / 10) * 10
            foody = round(random.randrange(0, height-10) / 10) * 10

            Length_of_snake += 1


        clock.tick(snake_speed)


    pygame.quit()
    quit()


gameLoop()