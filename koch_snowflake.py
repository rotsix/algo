#!/usr/bin/env python

"""
simple representation of the Koch snowflake
"""

import sys
import math
import pygame


BLACK = (0, 0, 0)
ANGLE = math.sqrt(3)/6


def grow(edges):
    for i in range(0, len(edges), 2):
        beg = edges[i]
        end = edges[i+1]

        # splits in 4 edges, like this : _/\_
        # so, there are 3 new nodes
        mid = ((end[0] + beg[0]) / 2, (end[1] + beg[1]) / 2)

        node1 = ((end[0] + beg[0]) * 1/3, (end[1] + beg[1]) * 1/3)
        node2 = (mid[0] - (end[1] - beg[1]) * ANGLE, mid[1] + (end[0] - beg[0]) * ANGLE)
        node3 = ((end[0] + beg[0]) * 2/3, (end[1] + beg[1]) * 2/3)

        edges.insert(i+1, node3)
        edges.insert(i+1, node2)
        edges.insert(i+1, node1)


def display(edges, screen):
    for edge in edges:
        pygame.draw.rect(screen,
                         BLACK,
                         [edge[0], edge[1], 1, 1])
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)


def main(args):
    """
    main loop
    """

    try:
        steps = int(args[1])
    except IndexError:
        steps = 10

    edges = [] # paires of coords

    edges.append((0., 0.))
    edges.append((1000., 0.))

    pygame.init()
    screen = pygame.display.set_mode([1000, 1000])
    pygame.display.set_caption("Koch Snowflake")
    screen.fill((255, 255, 255))

    for _ in range(steps):
        grow(edges)
        display(edges, screen)

    for i in edges:
        print(i)

if __name__ == "__main__":
    main(sys.argv)
