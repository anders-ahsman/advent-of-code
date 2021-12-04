#!/usr/bin/env python3

import sys
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(numbers: List[str]) -> int:
    gamma = ''
    epsilon = ''

    for i in range(len(numbers[0])):
        ones = ones_count(numbers, i)
        zeros = zeros_count(numbers, i)
        gamma += '1' if ones > zeros else '0'
        epsilon += '0' if ones > zeros else '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2(numbers: List[str]) -> int:
    def get_oxygen_rating(numbers: List[str]) -> int:
        for i in range(len(numbers[0])):
            more_ones = ones_count(numbers, i) >= zeros_count(numbers, i)
            numbers = numbers_with_one_at_idx(numbers, i) if more_ones else numbers_with_zero_at_idx(numbers, i)

            if len(numbers) == 1:
                return int(numbers[0], 2)
        raise ValueError()

    def get_scrubber_rating(numbers: List[str]) -> int:
        for i in range(len(numbers[0])):
            more_zeros = ones_count(numbers, i) < zeros_count(numbers, i)
            numbers = numbers_with_one_at_idx(numbers, i) if more_zeros else numbers_with_zero_at_idx(numbers, i)

            if len(numbers) == 1:
                return int(numbers[0], 2)
        raise ValueError()

    oxygen_rating = get_oxygen_rating(numbers)
    scrubber_rating = get_scrubber_rating(numbers)
    return oxygen_rating * scrubber_rating


def ones_count(numbers: List[str], idx: int) -> int:
    return sum(1 for number in numbers if number[idx] == '1')


def zeros_count(numbers: List[str], idx: int) -> int:
    return sum(1 for number in numbers if number[idx] == '0')


def numbers_with_one_at_idx(numbers: List[str], idx: int) -> List[str]:
    return [n for n in numbers if n[idx] == '1']


def numbers_with_zero_at_idx(numbers: List[str], idx: int) -> List[str]:
    return [n for n in numbers if n[idx] == '0']


if __name__ == '__main__':
    digits = read_input()
    print(f'Part 1: {part1(digits)}')
    print(f'Part 2: {part2(digits)}')
