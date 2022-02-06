#!/usr/bin/env python3

import sys
from typing import Dict, List


def read_input() -> List[str]:
    return [line.rstrip() for line in sys.stdin.readlines()]


def part1(lines: List[str]) -> int:
    chars_open_to_close: Dict[str, str] = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    chars_close_to_open: Dict[str, str] = {
         ')': '(',
         ']': '[',
         '}': '{',
         '>': '<',
    }
    chars_to_points: Dict[str, int] = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    def get_points_for_line(line: str) -> int:
        open_chunks_stack: List[str] = [line[0]]

        for char in line[1:]:
            if char in chars_open_to_close:
                open_chunks_stack.append(char)
                continue

            assert char in chars_close_to_open
            closes_last_open_chunk = open_chunks_stack[-1] == chars_close_to_open[char]
            if closes_last_open_chunk:
                open_chunks_stack.pop()
                continue

            return chars_to_points[char]

        return 0

    total_score = sum(get_points_for_line(line) for line in lines)
    return total_score


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {part1(lines)}')
