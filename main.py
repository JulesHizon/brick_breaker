import sys
import os
import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 350
PLATFORM_LENGTH = 100
PLATFORM_SPEED = 7.5

GALAXY = pygame.transform.scale(pygame.image.load(os.path.join('assets','galaxy.jpg')), (WIDTH, HEIGHT))

BRICK_ROW_1 = [((i+1)*50,50) for i in range(10)]
BRICK_ROW_2 = [((i+1)*50,70) for i in range(10)]
BRICK_ROW_3 = [((i+1)*50,90) for i in range(10)]
BRICK_ROW_4 = [((i+1)*50,110) for i in range(10)]

BRICK_GRID = [BRICK_ROW_1, BRICK_ROW_2, BRICK_ROW_3, BRICK_ROW_4]

BRICK_WIDTH = 50
BRICK_HEIGHT = 20

BRICK_COLOR = (124, 240, 124)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Breaker')

def draw_platform(platform):
    pygame.draw.rect(screen, (255,255,255), platform)

def draw_bricks():
    for row in BRICK_GRID:
        for col in row:
            brick = pygame.Rect(col[0], col[1], BRICK_WIDTH, BRICK_HEIGHT)
            pygame.draw.rect(screen, BRICK_COLOR, brick)
            pygame.draw.rect(screen, (0,0,0), brick, width=1)

def move_platform(keys_pressed, platform):
    if keys_pressed[pygame.K_LEFT]:
        platform.x -= PLATFORM_SPEED

    if keys_pressed[pygame.K_RIGHT]:
        platform.x += PLATFORM_SPEED

def show_background(platform):
    screen.blit(GALAXY, (0,0))
    draw_platform(platform)
    draw_bricks()
    pygame.display.update()

def main():
    platform = pygame.Rect(WIDTH/2 - PLATFORM_LENGTH, HEIGHT-50, PLATFORM_LENGTH, 10)
    active = True
    clock = pygame.time.Clock()
    while active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                pygame.quit()
        show_background(platform)

        keys_pressed = pygame.key.get_pressed()
        move_platform(keys_pressed, platform)

if __name__ == '__main__':
    main()