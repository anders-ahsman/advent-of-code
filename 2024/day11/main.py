#!/usr/bin/env python3

import sys
from functools import lru_cache


def read_input() -> list[int]:
    line = sys.stdin.readline()
    return list(map(int, line.split()))


def process_stones(stones: list[int], steps: int) -> int:
    return sum(expand_count(stone, steps) for stone in stones)


@lru_cache(None)
def expand_count(stone: int, steps: int) -> int:
    if steps == 0:
        return 1

    next_stones = process_stone(stone)
    return sum(expand_count(s, steps - 1) for s in next_stones)


@lru_cache(None)
def process_stone(stone: int) -> tuple[int, ...]:
    if stone == 0:
        return (1,)
    else:
        s = str(stone)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            left = int(s[:mid])
            right = int(s[mid:])
            return (left, right)
        else:
            return (stone * 2024,)


if __name__ == '__main__':
    stones = read_input()
    print(f'Part 1: {process_stones(stones, 25)}')
    print(f'Part 2: {process_stones(stones, 75)}')
