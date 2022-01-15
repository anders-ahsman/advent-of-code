#!/usr/bin/env python3

from __future__ import annotations

import sys
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, List, Optional, Tuple

Position = Tuple[int, int]


def read_input() -> List[List[int]]:
    return [[int(n) for n in line.strip()] for line in sys.stdin]


@dataclass
class Node:
    position: Position
    cost: int
    # heuristic not used

    def __lt__(self, other: Node) -> bool:
        return self.cost < other.cost


def a_star(risk_map: List[List[int]]) -> Optional[int]:
    def get_neighbours(p: Position) -> List[Position]:
        p_x, p_y = p
        neighbours: List[Position] = []
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            x = p_x + dx
            y = p_y + dy
            if 0 <= x < len(risk_map[0]) and 0 <= y < len(risk_map):
                neighbours.append((x, y))
        return neighbours

    frontier: List[Node] = []
    start_pos: Position = (0, 0)
    start_node: Node = Node(position=start_pos, cost=0)
    destination_pos: Position = (len(risk_map[0]) - 1, len(risk_map) - 1)

    heappush(frontier, start_node)
    dest_to_min_risk: Dict[Position, int] = {
        start_pos: 0
    }

    while frontier:
        current_node = heappop(frontier)
        if current_node.position == destination_pos:
            return current_node.cost

        for neighbour_pos in get_neighbours(current_node.position):
            neighbour_x, neighbour_y = neighbour_pos
            new_cost: int = risk_map[neighbour_y][neighbour_x] + current_node.cost

            if neighbour_pos not in dest_to_min_risk or new_cost < dest_to_min_risk[neighbour_pos]:
                dest_to_min_risk[neighbour_pos] = new_cost
                neighbour_node = Node(position=neighbour_pos, cost=new_cost)
                heappush(frontier, neighbour_node)

    return None


def enlarge_map(risk_map: List[List[int]]) -> List[List[int]]:
    size_small_map = len(risk_map)
    factor = 5
    size_large_map = size_small_map * factor
    risk_map_large = [[0] * size_large_map for _ in range(size_large_map)]

    for row_offset in range(factor):
        for col_offset in range(factor):
            for row_small_map in range(size_small_map):
                for col_small_map in range(size_small_map):
                    row = row_small_map + row_offset * size_small_map
                    col = col_small_map + col_offset * size_small_map
                    manhattan_dist = abs(row_small_map - row) + abs(col_small_map - col)
                    value = (risk_map[row_small_map][col_small_map] + manhattan_dist - 1) % 9 + 1
                    risk_map_large[row][col] = value

    return risk_map_large


if __name__ == '__main__':
    risk_map = read_input()
    print(f'Part 1: {a_star(risk_map)}')

    risk_map_large = enlarge_map(risk_map)
    print(f'Part 2: {a_star(risk_map_large)}')
