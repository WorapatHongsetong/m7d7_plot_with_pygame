import pygame
import math
import random
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def sine(x):
    return math.sin(x)

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
        x_real = x / 49.917 - 299
        y_real = (sine(x_real))
        y = int(299.5 * y_real +299.5)
        screen.set_at((int(x), int(y)), (255, 255, 255))
        if x > 0:
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x, y0))
        y0 = y

    pygame.display.flip()

pygame.quit()