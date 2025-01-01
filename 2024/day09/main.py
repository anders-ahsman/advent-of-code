#!/usr/bin/env python3

import sys


def read_input() -> str:
    for line in sys.stdin:
        return line.strip()

    raise ValueError('No input')


def part1(disk_map: str) -> int:
    data = decompress(disk_map)
    compress_data(data)
    checksum = calculate_checksum(data)

    return checksum


def decompress(disk_map: str) -> list[str]:
    data: list[str] = []
    is_file = True
    file_id = 0

    for char in disk_map:
        for _ in range(int(char)):
            data.append((str(file_id) if is_file else '.'))

        file_id += 1 if is_file else 0
        is_file = not is_file

    return data


def compress_data(data: list[str]) -> None:
    def leftmost_dot_idx(data: list[str]) -> int:
        return data.index('.')

    def rightmost_non_dot_idx(data: list[str]) -> int:
        for i in range(len(data) - 1, -1, -1):
            if data[i] != '.':
                return i
        return -1

    while True:
        left_idx = leftmost_dot_idx(data)
        right_idx = rightmost_non_dot_idx(data)
        if left_idx > right_idx:
            break

        data[left_idx], data[right_idx] = data[right_idx], data[left_idx]


def calculate_checksum(data: list[str]) -> int:
    checksum = 0
    for i, char in enumerate(data):
        if char != '.':
            checksum += i * int(char)

    return checksum


if __name__ == '__main__':
    disk_map = read_input()
    print(f'Part 1: {part1(disk_map)}')
