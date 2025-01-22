import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def square(x):
    return x ** 2

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))

    for x in range(0, 600):
        x_real = 0.00668 * x - 2
        y_real = (square(x_real))
        y = int(-74.875 * y_real +299.5)
        screen.set_at((int(x), int(y)), (255, 255, 255))
        # pygame.draw.line(screen, (0, 255, 0), (10, 10), (300, 300))

    pygame.display.flip()

pygame.quit()