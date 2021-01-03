from collections import defaultdict
from math import prod
import sys

import numpy as np


def read_tiles():
    tiles = {}
    sections = [l.split('\n') for l in sys.stdin.read().split('\n\n')]
    for tile_lines in sections:
        key = int(tile_lines[0].replace(':', '').replace('Tile ', ''))
        tiles[key] = np.array([list(line) for line in tile_lines[1:]])
    return tiles


def part1(tiles):
    tile_to_neighbours = defaultdict(set)
    for t1, a1 in tiles.items():
        for t2, a2 in tiles.items():
            if t1 == t2:
                continue
            for a2_comb in array_combinations(a2):
                if possible_neighbours(a1, a2_comb):
                    tile_to_neighbours[t1].add(t2)
    return prod(t for t in tile_to_neighbours if len(tile_to_neighbours[t]) == 2)


def array_combinations(a):
    for _ in range(4):
        a = np.rot90(a)
        yield a
    a = np.fliplr(a)
    for _ in range(4):
        a = np.rot90(a)
        yield a


def possible_neighbours(a1, a2):
    h, w = len(a1), len(a1[0])
    h_range = list(range(h))

    # a2 above a1
    if (a2[h - 1] == a1[0]).all():
        return True

    # a2 below a1
    if (a1[h - 1] == a2[0]).all():
        return True

    # a2 to the left of a1
    if ((a2[h_range, [w - 1]]) == a1[h_range, [0]]).all():
        return True

    # a2 to the right of a1
    if ((a1[h_range, [w - 1]]) == a2[h_range, [0]]).all():
        return True

    return False


if __name__ == '__main__':
    tiles = read_tiles()
    print(f'Part 1: {part1(tiles)}')