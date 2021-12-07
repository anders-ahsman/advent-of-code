#!/usr/bin/env python3

import sys
from functools import lru_cache, reduce
from typing import List, Optional


def read_crab_positions() -> List[int]:
    return [int(n) for n in next(sys.stdin).split(',')]


def part1(crab_posititions: List[int]) -> int:
    fuel_min: Optional[int] = None
    for pos in range(max(crab_posititions)):
        fuel = 0
        for crab_pos in crab_posititions:
            fuel += abs(pos - crab_pos)
        if not fuel_min or fuel < fuel_min:
            fuel_min = fuel
    return fuel_min


def part2(crab_posititions: List[int]) -> int:

    @lru_cache(maxsize=None)
    def calculate_cost(distance: int) -> int:
        return reduce(lambda a, b: a + b, range(distance + 1))

    fuel_min: Optional[int] = None
    for pos in range(max(crab_posititions)):
        fuel = 0
        for crab_pos in crab_posititions:
            distance = abs(pos - crab_pos)
            fuel += calculate_cost(distance)
        if not fuel_min or fuel < fuel_min:
            fuel_min = fuel
    return fuel_min


if __name__ == '__main__':
    crab_posititions = read_crab_positions()
    print(f'Part 1: {part1(crab_posititions)}')
    print(f'Part 2: {part2(crab_posititions)}')
