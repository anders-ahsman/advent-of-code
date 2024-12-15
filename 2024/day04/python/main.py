#!/usr/bin/env python3

import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def part1(document: list[str]) -> int:
    directions = (
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    seen = set()
    count = 0
    row_count = len(document)
    col_count = len(document[0])
    for iy in range(row_count):
        for ix in range(col_count):
            for dx, dy in directions:
                x, y = ix, iy
                if out_of_bounds(x, y, col_count, row_count):
                    continue

                word = document[y][x]
                while True:
                    x += dx
                    y += dy
                    if out_of_bounds(x, y, col_count, row_count):
                        break

                    word += document[y][x]
                    key = (x, y, dx, dy)
                    if word[-4:] in ('XMAS', 'SAMX') and key not in seen:
                        count += 1
                        seen.add(key)

    return count


def out_of_bounds(x: int, y: int, col_count: int, row_count: int) -> bool:
    return x < 0 or y < 0 or x >= col_count or y >= row_count


def part2(document: list[str]) -> int:
    count = 0
    row_count = len(document)
    col_count = len(document[0])

    chunk_size = 3
    for yi in range(row_count - chunk_size + 1):
        for xi in range(col_count - chunk_size + 1):
            chunk: list[str] = [document[y][xi : xi + chunk_size] for y in range(yi, yi + chunk_size)]
            if is_xmas_chunk(chunk):
                count += 1

    return count


def is_xmas_chunk(chunk: list[str]) -> bool:
    if chunk[1][1] != 'A':
        return False

    valid = {'SM', 'MS'}
    return chunk[0][0] + chunk[2][2] in valid and chunk[0][2] + chunk[2][0] in valid


if __name__ == '__main__':
    document = read_input()
    print(part1(document))
    print(part2(document))
