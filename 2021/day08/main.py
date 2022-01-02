#!/usr/bin/env python3

import sys
from typing import List


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(segments: List[str]) -> int:
    count = 0
    for entry in segments:
        signal_patterns, output = entry.split(' | ')
        for digit in output.split(' '):
            if len(digit) in (2, 3, 4, 7):
                count += 1
    return count


if __name__ == '__main__':
    input = read_input()
    print(f'Part 1: {part1(input)}')
