#!/usr/bin/env python3

import sys


def read_input() -> list[list[int]]:
    return [list(map(int, line.strip().split())) for line in sys.stdin]


def solve(reports: list[list[int]], part2: bool) -> int:
    safe = 0

    for report in reports:
        if is_safe(report):
            safe += 1
            continue
        elif part2:
            for i in range(len(report)):
                modified = report[:i] + report[i + 1 :]
                if is_safe(modified):
                    safe += 1
                    break

    return safe


def is_safe(report: list[int]) -> bool:
    increasing = 0
    decreasing = 0
    count = len(report) - 1
    for i in range(count):
        if 1 <= report[i + 1] - report[i] <= 3:
            increasing += 1
        elif 1 <= report[i] - report[i + 1] <= 3:
            decreasing += 1

    return (increasing == count) or (decreasing == count)


if __name__ == '__main__':
    reports = read_input()
    print(solve(reports, False))
    print(solve(reports, True))
