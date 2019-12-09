# first, pip install pygame
# then run

import pygame, sys, random
from pygame.locals import *

def on_grid_random():
    x= random.randint(0,1270)
    y= random.randint(0,710)
    return (x//10 * 10, y//10 * 10)

def collision(c1,c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))

UP=0
RIGHT=1
DOWN=2
LEFT=3


pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('ABACAXI')

snake = [(200, 200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0))

apple_pos=on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((0,0,0))

my_direction = LEFT

clock = pygame.time.Clock()
score = 0

while True:
    print(snake)

    if(score in range(0,5)):
        clock.tick(10)
    elif(score in range(5,10)):
        clock.tick(20)
    elif(score in range(10,15)):
        clock.tick(40)
    elif(score in range(15,20)):
        clock.tick(80)
    else:
        clock.tick(500)
    
    font = pygame.font.SysFont('arial', 32)
    textScore = "Sua cobrinha come bastante = " + str(score)
    text = font.render(textScore, True, (255,255,255), (200,100,100))
    textRect = text.get_rect()
    textRect.center = (800,30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT
    
    if collision(snake[0],apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        print("add no final")
        print(snake)
        score += 1
    
    if my_direction == UP:
        snake[0] = (snake[0][0], (snake[0][1] - 10) % 720 )
    if my_direction == DOWN:
        snake[0] = (snake[0][0], (snake[0][1] + 10)% 720)
    if my_direction == LEFT:
        snake[0] = ((snake[0][0] - 10) % 1280, snake[0][1])
    if my_direction == RIGHT:
        snake[0] = ((snake[0][0] + 10)% 1280, snake[0][1])
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    
    screen.fill((200,100,100))
    screen.blit(apple,apple_pos)
    screen.blit(text, textRect)
    for pos in snake:
        screen.blit(snake_skin,pos)
    

    pygame.display.update()

