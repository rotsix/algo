#!/usr/bin/env python

"""
Simple implementation of the Langton's Ant
https://en.wikipedia.org/wiki/Langton%27s_ant

usage: ./langtons_ant.py [width height]
"""

import sys
import pygame

WIDTH = 100 # default
HEIGHT = 100
CELL_SIZE = 5
MARGIN = 1
SCREEN = None

BLACK = (0, 0, 0)
GRAY_DARK = (63, 63, 63)
GRAY_LIGHT = (191, 191, 191)
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
    grid[HEIGHT//2][WIDTH//2] = GRAY_LIGHT

    # pygame
    pygame.init()
    global SCREEN
    SCREEN = pygame.display.set_mode([HEIGHT * (CELL_SIZE+MARGIN), WIDTH * (CELL_SIZE+MARGIN)])
    pygame.display.set_caption("Langton's Ant")
    SCREEN.fill((127, 127, 127))

    return grid


def grid_display(grid):
    """
    well.. display the grid?
    """
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pygame.draw.rect(SCREEN,
                             grid[i][j],
                             [(MARGIN + CELL_SIZE) * j + MARGIN,
                              (MARGIN + CELL_SIZE) * i + MARGIN,
                              CELL_SIZE,
                              CELL_SIZE])
    #pygame.time.Clock().tick(60)
    pygame.display.flip()


def grid_eval(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # pos[0]: width
            # pos[1]: height
            col = pos[0] // (CELL_SIZE + MARGIN)
            row = pos[1] // (CELL_SIZE + MARGIN)
            if grid[row][col] == WHITE:
                grid[row][col] = BLACK
            else:
                grid[row][col] = WHITE

    return False


def main(argv):
    """
    main loop, argv should contains the grid size, and step duration
    """
    grid = grid_init(argv)

    done = False
    while not done:
        done = grid_eval(grid)
        grid_display(grid)
        # sleep(0)

    pygame.quit()


if __name__ == "__main__":
    main(sys.argv)
