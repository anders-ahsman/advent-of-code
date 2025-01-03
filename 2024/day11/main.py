#!/usr/bin/env python3

import sys


def read_input() -> list[int]:
    line = sys.stdin.readline()
    return list(map(int, line.split()))


def part1(stones: list[int]) -> int:
    return process_stones(stones, 25)


def process_stones(stones: list[int], max_iter: int) -> int:
    for _ in range(max_iter):
        i = 0
        while i < len(stones):
            stone = stones[i]
            if stone == 0:
                stones[i] = 1
            elif len(str(stone)) % 2 == 0:
                idx = len(str(stone)) // 2
                left, right = int(str(stone)[:idx]), int(str(stone)[idx:])
                stones[i] = left
                stones.insert(i + 1, right)
                i += 1
            else:
                stones[i] = stone * 2024
            i += 1

    return len(stones)


if __name__ == '__main__':
    stones = read_input()
    print(f'Part 1: {part1(stones)}')
