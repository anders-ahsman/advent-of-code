#!/usr/bin/env python3

import sys
from typing import List


def read_board() -> List[List[int]]:
    return [[int(char) for char in line.strip()]
            for line in sys.stdin]


def part1(board: List[List[int]]) -> int:
    sum_risk_lowpoints = 0
    for y, row in enumerate(board):
        for x, num in enumerate(row):
            is_lowpoint = True
            if x - 1 >= 0 and num > board[y][x - 1]:
                is_lowpoint = False
            if x + 1 < len(board[y]) and num >= board[y][x + 1]:
                is_lowpoint = False
            if y - 1 >= 0 and num > board[y - 1][x]:
                is_lowpoint = False
            if y + 1 < len(board) and num >= board[y + 1][x]:
                is_lowpoint = False
            if is_lowpoint:
                sum_risk_lowpoints += num + 1
    return sum_risk_lowpoints


if __name__ == '__main__':
    board = read_board()
    print(f'Part 1: {part1(board)}')
