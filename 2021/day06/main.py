#!/usr/bin/env python3

import sys
from collections import deque
from typing import Deque, List


def read_lanternfish() -> List[int]:
    return [int(n) for n in next(sys.stdin).split(',')]


def simulate_fish_growth(fish: List[int], days: int) -> int:
    fish_days_until_procreation: Deque[int] = deque([fish.count(day) for day in range(7)])
    fish_offspring: Deque[int] = deque([0, 0, 0])  # one extra day, should not count offspring until next day

    for _ in range(days - 1):
        fish_days_until_procreation.rotate(-1)
        fish_days_until_procreation[6] += fish_offspring.popleft()

        fish_offspring.append(fish_days_until_procreation[0])

    return sum(fish_days_until_procreation) + sum(fish_offspring)


if __name__ == '__main__':
    fish = read_lanternfish()
    print(f'Part 1: {simulate_fish_growth(fish, 80)}')
    print(f'Part 2: {simulate_fish_growth(fish, 256)}')
