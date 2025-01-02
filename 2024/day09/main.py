#!/usr/bin/env python3

import sys
from typing import Optional


def read_input() -> str:
    for line in sys.stdin:
        return line.strip()

    raise ValueError('No input')


def part1(disk_map: str) -> int:
    data = decompress(disk_map)
    defragment_by_blocks(data)
    checksum = calculate_checksum(data)

    return checksum


def part2(disk_map: str) -> int:
    data = decompress(disk_map)
    defragment_by_files(data)
    checksum = calculate_checksum(data)

    return checksum


def decompress(disk_map: str) -> list[Optional[int]]:
    data: list[Optional[int]] = []
    is_file = True
    file_id = 0

    for char in disk_map:
        for _ in range(int(char)):
            data.append(file_id if is_file else None)

        file_id += 1 if is_file else 0
        is_file = not is_file

    return data


def defragment_by_blocks(data: list[Optional[int]]) -> None:
    def leftmost_dot_idx(data: list[Optional[int]]) -> int:
        return data.index(None)

    def rightmost_non_dot_idx(data: list[Optional[int]]) -> int:
        for i in range(len(data) - 1, -1, -1):
            if data[i] is not None:
                return i
        return -1

    while True:
        left_idx = leftmost_dot_idx(data)
        right_idx = rightmost_non_dot_idx(data)
        if left_idx > right_idx:
            break

        data[left_idx], data[right_idx] = data[right_idx], data[left_idx]


def defragment_by_files(data: list[Optional[int]]) -> None:
    max_file_id = max([d for d in data if d is not None])

    for file_id in range(max_file_id, -1, -1):
        file_idx = data.index(file_id)
        file_idx_stop = len(data)
        for i in range(file_idx + 1, len(data)):
            if data[i] != file_id:
                file_idx_stop = i
                break
        file_len = file_idx_stop - file_idx

        free_space_found = False
        free_space_idx = 0
        free_space_len = 0
        for i, block in enumerate(data):
            if block is None:
                free_space_len += 1
            else:
                free_space_len = 0

            if free_space_len == file_len:
                free_space_idx = i - file_len + 1
                free_space_found = True
                break

        if free_space_found and free_space_idx < file_idx:
            for i in range(file_len):
                data[free_space_idx + i], data[file_idx + i] = data[file_idx + i], data[free_space_idx + i]


def calculate_checksum(data: list[Optional[int]]) -> int:
    checksum = 0
    for i, char in enumerate(data):
        if char is not None:
            checksum += i * int(char)

    return checksum


if __name__ == '__main__':
    disk_map = read_input()
    print(f'Part 1: {part1(disk_map)}')
    print(f'Part 2: {part2(disk_map)}')
