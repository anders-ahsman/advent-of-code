#!/usr/bin/env python3

import sys
from collections import defaultdict
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(lines: List[str]) -> int:
    board = defaultdict(int)
    for line in lines:
        pos_from, pos_to = line.split(' -> ')
        from_x, from_y = [int(pos) for pos in pos_from.split(',')]
        to_x, to_y = [int(pos) for pos in pos_to.split(',')]
        if from_x == to_x:
            for y in range(min(from_y, to_y), max(from_y, to_y) + 1):
                board[(from_x, y)] += 1
        if from_y == to_y:
            for x in range(min(from_x, to_x), max(from_x, to_x) + 1):
                board[(x, from_y)] += 1
    return sum(1 for overlap in board.values() if overlap >= 2)


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {part1(lines)}')
