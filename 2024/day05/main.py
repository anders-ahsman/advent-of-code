#!/usr/bin/env python3
import sys
from collections import defaultdict
from typing import DefaultDict

RuleDict = DefaultDict[int, list[int]]
Update = list[int]


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def get_rules_and_updates(puzzle_input: list[str]) -> tuple[RuleDict, list[Update]]:
    rules: RuleDict = defaultdict(list)
    updates: list[Update] = []

    for line in puzzle_input:
        if '|' in line:
            before, after = line.split('|')
            rules[int(before)].append(int(after))
        elif line:
            updates.append([int(x) for x in line.split(',')])

    return rules, updates


def get_valid_and_invalid_updates(rules: RuleDict, updates: list[Update]) -> tuple[list[Update], list[Update]]:
    valid_updates: list[Update] = []
    invalid_updates: list[Update] = []

    for update in updates:
        valid = True
        seen_pages: list[int] = []
        for i, page in enumerate(update):
            seen_pages.append(page)

            if page not in rules:
                continue

            for prev_page in seen_pages:
                if prev_page in rules[page]:
                    valid = False
                    break

            for later_page in update[i + 1 :]:
                if later_page not in rules[page]:
                    valid = False
                    break

        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    return valid_updates, invalid_updates


def sum_middle_numbers(updates: list[Update]) -> int:
    return sum(update[len(update) // 2] for update in updates)


def part1(valid_updates: list[Update]) -> int:
    return sum_middle_numbers(valid_updates)


if __name__ == '__main__':
    puzzle_input = read_input()
    rules, updates = get_rules_and_updates(puzzle_input)
    valid_updates, invalid_updates = get_valid_and_invalid_updates(rules, updates)

    print(f'Part 1: {part1(valid_updates)}')
