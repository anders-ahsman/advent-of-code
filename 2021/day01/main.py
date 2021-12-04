#!/usr/bin/env python3

import sys
from typing import List


def read_input() -> List[int]:
    return [int(number) for number in sys.stdin]


def number_of_increases(depths: List[int]) -> int:
    return sum(1 for i, depth in enumerate(depths[1:]) if depth > depths[i] or i == 0)


def number_of_increases_sliding_window(depths: List[int]) -> int:
    count = 0
    for i in range(len(depths[3:])):
        first_window = sum(depths[i - 1:i + 2])
        second_window = sum(depths[i:i + 3])
        if second_window > first_window:
            count += 1
    return count


if __name__ == '__main__':
    depths = read_input()
    print(f'Part 1: {number_of_increases(depths)}')
    print(f'Part 2: {number_of_increases_sliding_window(depths)}')
