#!/usr/bin/env python3

import sys
from typing import Callable, List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(numbers: List[str]) -> int:
    gamma = ''
    epsilon = ''

    for idx in range(len(numbers[0])):
        ones = ones_count(numbers, idx)
        zeros = zeros_count(numbers, idx)
        gamma += '1' if ones > zeros else '0'
        epsilon += '0' if ones > zeros else '1'

    return int(gamma, 2) * int(epsilon, 2)


def part2(numbers: List[str]) -> int:
    def get_rating(numbers: List[str], bit_criteria: Callable[[List[str], int], List[str]]) -> int:
        for idx in range(len(numbers[0])):
            numbers = bit_criteria(numbers, idx)
            if len(numbers) == 1:
                return int(numbers[0], 2)
        raise ValueError()

    def criteria_oxygen_rating(numbers: List[str], idx: int) -> List[str]:
        more_ones = ones_count(numbers, idx) >= zeros_count(numbers, idx)
        return numbers_with_one_at_idx(numbers, idx) if more_ones else numbers_with_zero_at_idx(numbers, idx)

    def criteria_scrubber_rating(numbers: List[str], idx: int) -> List[str]:
        more_zeros = ones_count(numbers, idx) < zeros_count(numbers, idx)
        return numbers_with_one_at_idx(numbers, idx) if more_zeros else numbers_with_zero_at_idx(numbers, idx)

    oxygen_rating = get_rating(numbers, criteria_oxygen_rating)
    scrubber_rating = get_rating(numbers, criteria_scrubber_rating)
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
