#!/usr/bin/env python3

import sys
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int
    height: int


def read_input() -> list[list[int]]:
    return [list(map(int, line.strip())) for line in sys.stdin]


def parse_raw_map(map_raw: list[list[int]]) -> list[Position]:
    map_topo: list[Position] = []

    for y in range(len(map_raw)):
        for x in range(len(map_raw[y])):
            h = map_raw[y][x]
            map_topo.append(Position(x, y, h))

    return map_topo


def part1(map_topo: list[Position]) -> int:
    trail_heads = [pos for pos in map_topo if pos.height == 0]

    return find_path_count(map_topo, trail_heads)


def part2(map_topo: list[Position]) -> int:
    trail_heads = [pos for pos in map_topo if pos.height == 0]

    return find_possible_path_count(map_topo, trail_heads)


def find_path_count(map_topo: list[Position], trail_heads: list[Position]) -> int:
    path_count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for trail_head in trail_heads:
        visited: set[Position] = set()
        queue: deque[Position] = deque([trail_head])

        while queue:
            pos = queue.popleft()

            if pos.height == 9:
                path_count += 1
                continue

            for dx, dy in directions:
                new_pos = Position(pos.x + dx, pos.y + dy, pos.height + 1)
                if new_pos not in visited and new_pos in map_topo:
                    visited.add(new_pos)
                    queue.append(new_pos)

    return path_count


def find_possible_path_count(map_topo: list[Position], trail_heads: list[Position]) -> int:
    path_count = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for trail_head in trail_heads:
        queue: deque[list[Position]] = deque([[trail_head]])

        while queue:
            path = queue.popleft()
            pos = path[-1]

            if pos.height == 9:
                path_count += 1
                continue

            for dx, dy in directions:
                new_pos = Position(pos.x + dx, pos.y + dy, pos.height + 1)
                if new_pos in map_topo:
                    new_path = path + [new_pos]
                    queue.append(new_path)

    return path_count


if __name__ == '__main__':
    map_raw = read_input()
    map_topo = parse_raw_map(map_raw)
    print(f'Part 1: {part1(map_topo)}')
    print(f'Part 2: {part2(map_topo)}')
