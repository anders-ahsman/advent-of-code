#!/usr/bin/env python3

import sys
from collections import defaultdict
from typing import DefaultDict, List, Set


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin]


def part1(lines: List[str]) -> int:
    connections: DefaultDict[str, Set[str]] = defaultdict(set)
    for line in lines:
        start, end = line.split('-')
        connections[start].add(end)
        connections[end].add(start)

    path_count = 0

    def visit_node(node: str, path: List[str], explored: Set[str]) -> None:
        explored.add(node)

        if node == 'end':
            nonlocal path_count
            path_count += 1
            return

        for neighbour_node in connections[node]:
            if neighbour_node.isupper() or (neighbour_node.islower() and neighbour_node not in explored):
                visit_node(neighbour_node, path + [node], explored.copy())

    visit_node('start', [], set())

    return path_count


if __name__ == '__main__':
    input = read_input()
    print(f'Part 1: {part1(input)}')
