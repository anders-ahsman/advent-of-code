#!/usr/bin/env python3

import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Board:
    width: int
    height: int


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Antenna:
    pos: Position
    frequency: str


def read_input() -> tuple[set[Antenna], Board]:
    width = 0
    height = 0
    antennas: set[Antenna] = set()

    for y, line in enumerate(sys.stdin):
        line = line.strip()
        for x, char in enumerate(line):
            if char.isalnum():
                antennas.add(Antenna(Position(x, y), char))
            elif char == '.':
                pass
            else:
                raise ValueError(f'Invalid character: {char}')

            width = max(width, x)
            height = max(height, y)

    board = Board(width, height)

    return antennas, board


def part1(antennas: set[Antenna], board: Board) -> int:
    antinode_positions: set[Position] = set()

    for a1 in antennas:
        for a2 in antennas:
            if a1 != a2 and a1.frequency == a2.frequency:
                antinode = Position(2 * a1.pos.x - a2.pos.x, 2 * a1.pos.y - a2.pos.y)
                if not out_of_bounds(antinode, board):
                    antinode_positions.add(antinode)

    return len(antinode_positions)


def out_of_bounds(pos: Position, board: Board) -> bool:
    return pos.x < 0 or pos.x > board.width or pos.y < 0 or pos.y > board.height


if __name__ == '__main__':
    antennas, board = read_input()
    print(f'Part 1: {part1(antennas, board)}')
