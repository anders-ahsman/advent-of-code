#!/usr/bin/env python3

import sys
from collections import deque
from functools import reduce
from typing import Deque, List, Set, Tuple


Board = List[List[int]]
Position = Tuple[int, int]


def read_board() -> Board:
    return [[int(char) for char in line.strip()]
            for line in sys.stdin]


def part1(board: Board) -> int:
    sum_risk_lowpoints = 0
    for y, row in enumerate(board):
        for x, num in enumerate(row):
            is_lowpoint = not(
                (y - 1 >= 0 and num > board[y - 1][x]) or
                (y + 1 < len(board) and num >= board[y + 1][x]) or
                (x - 1 >= 0 and num > board[y][x - 1]) or
                (x + 1 < len(board[y]) and num >= board[y][x + 1]))
            if is_lowpoint:
                sum_risk_lowpoints += num + 1
    return sum_risk_lowpoints


def part2(board: Board) -> int:
    basin_sizes: List[int] = []
    visited: Set[Position] = set()

    for y_start in range(len(board)):
        for x_start in range(len(board[y_start])):
            basin_size = 0
            queue: Deque[Position] = deque([(x_start, y_start)])
            while queue:
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue

                visited.add((x, y))
                if board[y][x] != 9:
                    basin_size += 1
                    for neighbour in get_neighbours(board, x, y):
                        queue.append(neighbour)

            # no more connected positions to visit => basin completed
            if basin_size > 0:
                basin_sizes.append(basin_size)

    return reduce(lambda a, b: a * b, list(reversed(sorted(basin_sizes)))[:3])


def get_neighbours(board: Board, x: int, y: int) -> List[Position]:
    neighbours = []
    if y - 1 >= 0:
        neighbours.append((x, y - 1))
    if y + 1 < len(board):
        neighbours.append((x, y + 1))
    if x - 1 >= 0:
        neighbours.append((x - 1, y))
    if x + 1 < len(board[y]):
        neighbours.append((x + 1, y))
    return neighbours


if __name__ == '__main__':
    board = read_board()
    print(f'Part 1: {part1(board)}')
    print(f'Part 2: {part2(board)}')
