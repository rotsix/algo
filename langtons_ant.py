#!/usr/bin/env python

"""
Simple implementation of the Langton's Ant
https://en.wikipedia.org/wiki/Langton%27s_ant

usage: ./langtons_ant.py [width height]
"""

import sys
import pygame

WIDTH = 100 # default values
HEIGHT = 100
CELL_SIZE = 5
MARGIN = 1
SCREEN = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def grid_init(argv):
    """
    initialize the grid with 0s
    display it using grid_display
    """
    try:
        global WIDTH
        global HEIGHT
        WIDTH = argv[1]
        HEIGHT = argv[2]
    except IndexError:
        pass

    grid = [[WHITE for i in range(WIDTH)] for i in range(HEIGHT)]
    grid[HEIGHT//2][WIDTH//2] = RED

    # pygame
    pygame.init()
    global SCREEN
    SCREEN = pygame.display.set_mode([HEIGHT * (CELL_SIZE+MARGIN), WIDTH * (CELL_SIZE+MARGIN)])
    pygame.display.set_caption("Langton's Ant")
    SCREEN.fill(BLACK)

    return grid


def grid_display(grid):
    """
    well.. display the grid?
    """
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pygame.draw.rect(SCREEN,
                             grid[i][j],
                             [(MARGIN + WIDTH) * j + MARGIN,
                              (MARGIN + HEIGHT) * i + MARGIN,
                              WIDTH,
                              HEIGHT])
    pygame.time.Clock().tick(60)
    pygame.display.flip()


def grid_eval(grid):
    pass


def main(argv):
    """
    main loop, argv should contains the grid size, and step duration
    """
    grid = grid_init(argv)

    while True:
        grid_eval(grid)
        grid_display(grid)


if __name__ == "__main__":
    main(sys.argv)
