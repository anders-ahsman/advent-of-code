#!/usr/bin/env python3

import sys


def read_input() -> list[list[int]]:
    return [list(map(int, line.strip().split())) for line in sys.stdin]


def solve_part1(reports: list[list[int]]) -> int:
    safe = 0

    for report in reports:
        increasing = 0
        decreasing = 0
        count = len(report) - 1
        for i in range(count):
            if 1 <= report[i + 1] - report[i] <= 3:
                increasing += 1
            elif 1 <= report[i] - report[i + 1] <= 3:
                decreasing += 1

        if increasing == count or decreasing == count:
            safe += 1

    return safe


if __name__ == '__main__':
    reports = read_input()
    print(solve_part1(reports))
