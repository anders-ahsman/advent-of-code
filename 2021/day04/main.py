#!/usr/bin/env python3

import sys
from typing import List, Tuple

Board = List[List[int]]


class BingoBoard:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.BOARD_SIZE = len(board)  # assume square board
        self.is_marked = [[False] * self.BOARD_SIZE for _ in range(self.BOARD_SIZE)]

    def mark_position(self, row: int, col: int) -> None:
        self.is_marked[row][col] = True

    @property
    def has_bingo(self) -> bool:
        # horizontal
        for row in range(self.BOARD_SIZE):
            if all(is_marked for is_marked in self.is_marked[row]):
                return True

        # vertical
        for col in range(self.BOARD_SIZE):
            if all([self.is_marked[row][col] for row in range(self.BOARD_SIZE)]):
                return True

        return False

    @property
    def unmarked_sum(self) -> int:
        return sum(self.board[row][col]
                   for col in range(self.BOARD_SIZE)
                   for row in range(self.BOARD_SIZE)
                   if not self.is_marked[row][col])


def read_numbers_and_bingo_boards() -> Tuple[List[int], List[BingoBoard]]:
    lines = [line.strip() for line in sys.stdin]

    numbers = [int(num) for num in lines[0].split(',')]

    boards: List[Board] = []
    board: Board = []
    for line in lines[1:] + ['']:  # add extra empty line to include last board
        if line != '':
            board.append([int(num) for num in line.split()])
        else:
            boards.append(board)
            board = []

    bingo_boards = [BingoBoard(board) for board in boards]
    return numbers, bingo_boards


def part1(numbers: List[int], bingo_boards: List[BingoBoard]) -> int:
    for number in numbers:
        for bingo_board in bingo_boards:
            for row_idx, row in enumerate(bingo_board.board):
                for col_idx, board_number in enumerate(row):
                    if board_number == number:
                        bingo_board.mark_position(row_idx, col_idx)
                        if bingo_board.has_bingo:
                            return number * bingo_board.unmarked_sum
    raise ValueError('No board had bingo!')


def part2(numbers: List[int], bingo_boards: List[BingoBoard]) -> int:
    last_score = 0
    for number in numbers:
        for bingo_board in bingo_boards:
            if bingo_board.has_bingo:
                continue
            for row_idx, row in enumerate(bingo_board.board):
                for col_idx, board_number in enumerate(row):
                    if board_number == number:
                        bingo_board.mark_position(row_idx, col_idx)
                        if bingo_board.has_bingo:
                            last_score = number * bingo_board.unmarked_sum
    return last_score


if __name__ == '__main__':
    numbers, bingo_boards = read_numbers_and_bingo_boards()
    print(f'Part 1: {part1(numbers, bingo_boards)}')
    print(f'Part 2: {part2(numbers, bingo_boards)}')
