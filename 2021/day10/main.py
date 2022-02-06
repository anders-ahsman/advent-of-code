#!/usr/bin/env python3

import sys
from typing import Dict, List


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
chars_to_syntax_errors_points: Dict[str, int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
chars_to_autocomplete_points: Dict[str, int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def read_input() -> List[str]:
    return [line.rstrip() for line in sys.stdin.readlines()]


def part1(lines: List[str]) -> int:
    def get_syntax_error_score(line: str) -> int:
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

            return chars_to_syntax_errors_points[char]

        # valid line
        return 0

    total_score = sum(get_syntax_error_score(line) for line in lines)
    return total_score


def part2(lines: List[str]) -> int:
    def get_autocomplete_score(line: str) -> int:
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

            # syntax error
            return 0

        score: int = 0
        while open_chunks_stack:
            last_char = open_chunks_stack.pop()
            assert last_char in chars_open_to_close
            char_score = chars_to_autocomplete_points[chars_open_to_close[last_char]]
            score = (score * 5) + char_score

        return score

    line_scores: List[int] = sorted([score for line in lines if (score := get_autocomplete_score(line))])
    middle_score: int = line_scores[len(line_scores) // 2]
    return middle_score


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
