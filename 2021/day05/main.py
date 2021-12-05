#!/usr/bin/env python3

import sys
from collections import defaultdict
from typing import DefaultDict, List, Tuple


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1_and_2(lines: List[str], include_diagonal_lines: bool) -> int:
    board: DefaultDict[Tuple[int, int], int] = defaultdict(int)

    for line in lines:
        pos_from, pos_to = line.split(' -> ')
        from_x, from_y = [int(pos) for pos in pos_from.split(',')]
        to_x, to_y = [int(pos) for pos in pos_to.split(',')]
        if from_x == to_x:  # vertical line
            for y in range(min(from_y, to_y), max(from_y, to_y) + 1):
                board[(from_x, y)] += 1
        elif from_y == to_y:  # horizontal line
            for x in range(min(from_x, to_x), max(from_x, to_x) + 1):
                board[(x, from_y)] += 1
        elif include_diagonal_lines:  # assume diagonal 45 degrees
            for step in range(max(from_y, to_y) - min(from_y, to_y) + 1):
                pos_x = from_x + step * (1 if to_x > from_x else -1)
                pos_y = from_y + step * (1 if to_y > from_y else -1)
                board[(pos_x, pos_y)] += 1
    return sum(1 for overlap in board.values() if overlap >= 2)


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {part1_and_2(lines, False)}')
    print(f'Part 2: {part1_and_2(lines, True)}')
