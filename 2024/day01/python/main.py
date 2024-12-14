#!/usr/bin/env python3

import sys


def read_input() -> list[tuple[int, int]]:
    return [tuple(map(int, line.strip().split())) for line in sys.stdin]


def extract_location_ids(location_ids: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for location_id in location_ids:
        left.append(location_id[0])
        right.append(location_id[1])
    left.sort()
    right.sort()

    return left, right


def solve_part1(left: list[int], right: list[int]) -> int:
    diffs = [abs(left[i] - right[i]) for i in range(len(left))]

    return sum(diffs)


def solve_part2(left: list[int], right: list[int]) -> int:
    scores = [location_id * right.count(location_id) for location_id in left]

    return sum(scores)

if __name__ == '__main__':
    left, right = extract_location_ids(read_input())

    print(solve_part1(left, right))
    print(solve_part2(left, right))