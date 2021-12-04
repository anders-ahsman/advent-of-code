#!/usr/bin/env python3

import sys
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(instructions: List[str]) -> int:
    x = 0
    y = 0

    for instruction in instructions:
        direction, value = instruction.split(' ')
        value = int(value)
        if direction == 'forward':
            x += value
        elif direction == 'down':
            y += value
        elif direction == 'up':
            y -= value

    return x * y


def part2(instructions: List[str]) -> int:
    x = 0
    y = 0
    aim = 0

    for instruction in instructions:
        direction, value = instruction.split(' ')
        value = int(value)
        if direction == 'forward':
            x += value
            y += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value

    return x * y


if __name__ == '__main__':
    instructions = read_input()
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')
