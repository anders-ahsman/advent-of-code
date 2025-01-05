#!/usr/bin/env python3

import sys
from collections import defaultdict, deque
from dataclasses import dataclass

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Region:
    plant: str
    positions: list[Position]


def read_input() -> list[list[str]]:
    return [list(map(str, line.strip())) for line in sys.stdin]


def extract_connected_regions(map_raw: list[list[str]]) -> list[Region]:
    positions_by_plant: defaultdict[str, list[Position]] = defaultdict(list)
    for y in range(len(map_raw)):
        for x in range(len(map_raw[y])):
            pos = Position(x, y)
            plant = map_raw[y][x]
            positions_by_plant[plant].append(pos)

    regions: list[Region] = []
    for plant, positions in positions_by_plant.items():
        position_set = set(positions)
        visited: set[Position] = set()

        for pos in positions:
            if pos in visited:
                continue

            queue: deque[Position] = deque([pos])
            connected: list[Position] = []

            while queue:
                current = queue.popleft()
                if current in visited:
                    continue

                visited.add(current)
                connected.append(current)

                for dx, dy in DIRECTIONS:
                    new_pos = Position(current.x + dx, current.y + dy)
                    if new_pos in position_set and new_pos not in visited:
                        queue.append(new_pos)

            regions.append(Region(plant, connected))

    return regions


def part1(regions: list[Region]) -> int:
    total_price = 0
    all_positions = set([p for r in regions for p in r.positions])

    for region in regions:
        other_regions = [r for r in regions if r != region]
        positions_outside_region = set([p for region in other_regions for p in region.positions])
        perimeter = 0

        for pos in region.positions:
            for dx, dy in DIRECTIONS:
                new_pos = Position(pos.x + dx, pos.y + dy)
                if new_pos in positions_outside_region or new_pos not in all_positions:
                    perimeter += 1

        total_price += perimeter * len(region.positions)

    return total_price


if __name__ == '__main__':
    raw_map = read_input()
    regions = extract_connected_regions(raw_map)
    print(f'Part 1: {part1(regions)}')
