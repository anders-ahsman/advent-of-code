#!/usr/bin/env python3

import sys
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(numbers: List[str]) -> int:
    gamma = ''
    epsilon = ''

    for i in range(len(numbers[0])):
        ones = sum(1 for number in numbers if number[i] == '1')
        zeros = sum(1 for number in numbers if number[i] == '0')
        gamma += '1' if ones > zeros else '0'
        epsilon += '0' if ones > zeros else '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2(numbers: List[str]) -> int:
    def get_oxygen_rating(numbers: List[str]) -> int:
        for i in range(len(numbers[0])):
            ones = sum(1 for number in numbers if number[i] == '1')
            zeros = sum(1 for number in numbers if number[i] == '0')
            if ones >= zeros:
                numbers = [n for n in numbers if n[i] == '1']
            else:
                numbers = [n for n in numbers if n[i] == '0']

            if len(numbers) == 1:
                return int(numbers[0], 2)
        raise ValueError()

    def get_scrubber_rating(numbers: List[str]) -> int:
        for i in range(len(numbers[0])):
            ones = sum(1 for number in numbers if number[i] == '1')
            zeros = sum(1 for number in numbers if number[i] == '0')
            if ones < zeros:
                numbers = [n for n in numbers if n[i] == '1']
            else:
                numbers = [n for n in numbers if n[i] == '0']

            if len(numbers) == 1:
                return int(numbers[0], 2)
        raise ValueError()

    oxygen_rating = get_oxygen_rating(numbers)
    scrubber_rating = get_scrubber_rating(numbers)
    return oxygen_rating * scrubber_rating


if __name__ == '__main__':
    digits = read_input()
    print(f'Part 1: {part1(digits)}')
    print(f'Part 2: {part2(digits)}')
