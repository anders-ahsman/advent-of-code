#!/usr/bin/env python3

import re
import sys

pattern_mul = re.compile(r'mul\((\d+),(\d+)\)')
pattern_do = re.compile(r'do\(\)')
pattern_dont = re.compile(r'don\'t\(\)')


def read_input() -> str:
    lines = [line.strip() for line in sys.stdin]
    return ''.join(lines)


def part1(memory: str) -> int:
    matches = re.findall(pattern_mul, memory)
    sum = 0
    for match in matches:
        x, y = map(int, match)
        sum += x * y

    return sum


def part2(memory: str) -> int:
    sum = 0
    pos = 0
    is_on = True

    while pos < len(memory):
        memory_chunk = memory[pos:]
        match_mul = re.search(pattern_mul, memory_chunk)
        match_do = re.search(pattern_do, memory_chunk)
        match_dont = re.search(pattern_dont, memory_chunk)

        next_mul = match_mul.start() if match_mul else len(memory)
        next_do = match_do.start() if match_do else len(memory)
        next_dont = match_dont.start() if match_dont else len(memory)

        if match_mul and next_mul < next_do and next_mul < next_dont:
            if is_on:
                x, y = map(int, match_mul.groups())
                sum += x * y
            pos += match_mul.end()
        elif match_do and next_do < next_mul and next_do < next_dont:
            is_on = True
            pos += match_do.end()
        elif match_dont and next_dont < next_mul and next_dont < next_do:
            is_on = False
            pos += match_dont.end()
        else:
            break

    return sum


if __name__ == '__main__':
    memory = read_input()
    print(part1(memory))
    print(part2(memory))
