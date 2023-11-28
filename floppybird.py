import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
GROUND_HEIGHT = 50
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")
background_img = pygame.image.load("background.png")
ground_img = pygame.image.load("ground.png")

bird_img = pygame.transform.scale(bird_img, (50, 50))
pipe_img = pygame.transform.scale(pipe_img, (50, 300))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
ground_img = pygame.transform.scale(ground_img, (WIDTH, GROUND_HEIGHT))

bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 1
jump_strength = 15

pipes = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_velocity = -jump_strength

    bird_y += bird_velocity
    bird_velocity += gravity

    if bird_y >= HEIGHT - GROUND_HEIGHT:
        bird_y = HEIGHT - GROUND_HEIGHT
        bird_velocity = 0

    if random.randint(0, 100) < 5:
        pipes.append(WIDTH)

    for pipe in pipes:
        pipe -= 5

    pipes = [pipe for pipe in pipes if pipe > -50]

    screen.blit(background_img, (0, 0))

    for pipe in pipes:
        screen.blit(pipe_img, (pipe, HEIGHT - GROUND_HEIGHT - 300))

    screen.blit(ground_img, (0, HEIGHT - GROUND_HEIGHT))
    screen.blit(bird_img, (bird_x, bird_y))

    pygame.display.flip()

    clock.tick(FPS)
