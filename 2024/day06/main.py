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
    width: int
    height: int


@dataclass(frozen=True)
class Guard:
    pos: Position
    dir: Direction


def read_input() -> tuple[set[Position], Guard, Board]:
    width = 0
    height = 0
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

            width = max(width, x)
            height = max(height, y)

    board = Board(width, height)

    return obstructions, guard, board


def part1(obstructions: set[Position], guard: Guard, board: Board) -> int:
    seen: set[Position] = set()

    while is_within_bounds(guard, board):
        seen.add(guard.pos)
        new_pos = get_next_guard_position(guard)
        if new_pos in obstructions:
            guard = Guard(guard.pos, turn_right(guard.dir))
        else:
            guard = Guard(new_pos, guard.dir)

    return len(seen)


def is_within_bounds(guard: Guard, board: Board) -> bool:
    return guard.pos.x >= 0 and guard.pos.x <= board.width and guard.pos.y >= 0 and guard.pos.y <= board.height


def get_next_guard_position(guard: Guard) -> Position:
    return Position(guard.pos.x + guard.dir.x, guard.pos.y + guard.dir.y)


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


def part2(obstructions: set[Position], guard: Guard, board: Board) -> int:
    count = 0
    obstructions_original: set[Position] = obstructions.copy()

    for y in range(board.height + 1):
        for x in range(board.width + 1):
            new_obstruction = Position(x, y)
            if new_obstruction not in obstructions and new_obstruction != guard.pos:
                obstructions = obstructions_original.copy()
                obstructions.add(new_obstruction)
                if is_loop(obstructions, guard, board):
                    count += 1

    return count


def is_loop(obstructions: set[Position], guard: Guard, board: Board) -> bool:
    trail: set[Guard] = set()

    while is_within_bounds(guard, board) and guard not in trail:
        trail.add(guard)
        new_pos = get_next_guard_position(guard)
        if new_pos in obstructions:
            guard = Guard(guard.pos, turn_right(guard.dir))
        else:
            guard = Guard(new_pos, guard.dir)

    return guard in trail


if __name__ == '__main__':
    obstructions, guard, board = read_input()
    print(f'Part 1: {part1(obstructions, guard, board)}')
    print(f'Part 2: {part2(obstructions, guard, board)}')
