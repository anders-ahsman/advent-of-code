#!/usr/bin/env python3

import sys
from typing import Dict, List, Tuple

Position = Tuple[int, int]


def read_input() -> List[List[int]]:
    return [[int(n) for n in line.strip()] for line in sys.stdin]


def part1(map: List[List[int]]) -> int:
    pos_to_dest_min_risk: Dict[Position, int] = {}

    def get_neighbours(p: Position) -> List[Position]:
        p_x, p_y = p

        neighbours: List[Position] = []
        if p_x + 1 < len(map[0]):
            neighbours.append((p_x + 1, p_y))
        if p_y + 1 < len(map):
            neighbours.append((p_x, p_y + 1))

        return neighbours

    def lowest_risk_to_dest(pos: Position, dest_pos: Position) -> None:
        pos_x, pos_y = pos

        # don't count initial position
        risk = map[pos_y][pos_x] if pos != (0, 0) else 0

        if pos == dest_pos:
            pos_to_dest_min_risk[pos] = risk
            return

        min_risk_to_neighbours = 999999
        for neighbour_pos in get_neighbours(pos):
            if neighbour_pos not in pos_to_dest_min_risk:
                lowest_risk_to_dest(neighbour_pos, dest_pos)
            min_risk_to_neighbours = min(pos_to_dest_min_risk[neighbour_pos], min_risk_to_neighbours)

        pos_to_dest_min_risk[pos] = risk + min_risk_to_neighbours

    start_pos = (0, 0)
    destination_pos = (len(map[0]) - 1, len(map) - 1)
    lowest_risk_to_dest(pos=start_pos, dest_pos=destination_pos)

    return pos_to_dest_min_risk[start_pos]


if __name__ == '__main__':
    map = read_input()
    print(f'Part 1: {part1(map)}')
