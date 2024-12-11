#!/usr/bin/env python3

import re
import sys


def read_input() -> str:
    lines = [line.strip() for line in sys.stdin]
    return ''.join(lines)


def solve(memory: str, part2: bool) -> int:
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, memory)
    sum = 0
    for match in matches:
        x, y = map(int, match)
        sum += x * y

    return sum


if __name__ == '__main__':
    memory = read_input()
    print(solve(memory, False))
    # print(solve(memory, True))
