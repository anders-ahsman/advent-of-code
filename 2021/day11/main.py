#!/usr/bin/env python3

import sys
from typing import List, Set, Tuple

Board = List[List[int]]
Position = Tuple[int, int]


def read_board() -> Board:
    return [[int(char) for char in line.strip()]
            for line in sys.stdin]


def part1(board: Board) -> int:
    total_flashes: int = 0

    for _ in range(100):
        # increase energy on all
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] += 1

        # keep going until flashes stop
        has_flashed_this_step: Set[Position] = set()
        while True:
            flash_count_before_step: int = len(has_flashed_this_step)
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] > 9 and (x, y) not in has_flashed_this_step:
                        has_flashed_this_step.add((x, y))
                        for nb_x, nb_y in get_neighbours(board, x, y):
                            if (nb_x, nb_y) not in has_flashed_this_step:
                                board[nb_y][nb_x] += 1

            flash_count_after_step: int = len(has_flashed_this_step)
            if flash_count_after_step == flash_count_before_step:
                break  # no change, step is complete

        # reset energy on all that flashed
        for x, y in has_flashed_this_step:
            board[y][x] = 0

        total_flashes += len(has_flashed_this_step)

    return total_flashes


def get_neighbours(board: Board, x: int, y: int) -> List[Position]:
    neighbours: List[Position] = []
    positions = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    for pos_x, pos_y in positions:
        if 0 <= pos_y < len(board) and 0 <= pos_x < len(board[0]):
            neighbours.append((pos_x, pos_y))
    return neighbours


if __name__ == '__main__':
    board = read_board()
    print(f'Part 1: {part1(board)}')
