#!/usr/bin/env python3

import sys
from typing import List


def read_lanternfish() -> List[int]:
    return [int(n) for n in next(sys.stdin).split(',')]


def part1(fish: List[int]) -> int:
    day = 1
    while day <= 80:
        new_fish: List[int] = []
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] = 6
                new_fish.append(8)
        fish += new_fish
        day += 1
    return len(fish)


if __name__ == '__main__':
    fish = read_lanternfish()
    print(f'Part 1: {part1(fish)}')
