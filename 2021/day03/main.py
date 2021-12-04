#!/usr/bin/env python3

import sys
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(numbers: List[str]) -> int:
    gamma = ''
    epsilon = ''

    for i in range(len(numbers[0])):
        zeros = sum(1 for number in numbers if number[i] == '0')
        ones = sum(1 for number in numbers if number[i] == '1')
        gamma += '1' if ones > zeros else '0'
        epsilon += '0' if ones > zeros else '1'

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    digits = read_input()
    print(f'Part 1: {part1(digits)}')
