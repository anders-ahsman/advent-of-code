#!/usr/bin/env python3

import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Direction:
    x: int
    y: int


@dataclass(frozen=True)
class Board:
    max_x: int
    max_y: int


@dataclass(frozen=True)
class Guard:
    pos: Position
    dir: Direction


def read_input() -> tuple[set[Position], Guard, Board]:
    max_x = 0
    max_y = 0
    obstructions: set[Position] = set()
    guard: Guard = Guard(Position(0, 0), Direction(0, 0))

    for y, line in enumerate(sys.stdin):
        line = line.strip()
        for x, char in enumerate(line):
            if char == '#':
                obstructions.add(Position(x, y))
            elif char == '^':
                guard = Guard(Position(x, y), Direction(0, -1))
            elif char == '.':
                pass
            else:
                raise ValueError(f'Invalid character: {char}')

            max_x = max(max_x, x)
            max_y = max(max_y, y)

    board = Board(max_x, max_y)

    return obstructions, guard, board


def part1(obstructions: set[Position], guard: Guard, board: Board) -> int:
    seen: set[Position] = set()

    while guard.pos.x >= 0 and guard.pos.x <= board.max_x and guard.pos.y >= 0 and guard.pos.y <= board.max_y:
        seen.add(guard.pos)
        new_pos = Position(guard.pos.x + guard.dir.x, guard.pos.y + guard.dir.y)
        if new_pos in obstructions:
            guard = Guard(guard.pos, turn_right(guard.dir))
        else:
            guard = Guard(new_pos, guard.dir)

    return len(seen)


def turn_right(dir: Direction) -> Direction:
    if dir == Direction(0, -1):
        return Direction(1, 0)
    elif dir == Direction(1, 0):
        return Direction(0, 1)
    elif dir == Direction(0, 1):
        return Direction(-1, 0)
    elif dir == Direction(-1, 0):
        return Direction(0, -1)
    else:
        raise ValueError(f'Invalid direction: {dir}')


if __name__ == '__main__':
    obstructions, guard, board = read_input()
    print(f'Part 1: {part1(obstructions, guard, board)}')
