#!/usr/bin/env python3

from collections import defaultdict
import sys
from typing import DefaultDict, Dict, Tuple


def read_input() -> Tuple[str, Dict[str, str]]:
    lines = [line.strip() for line in sys.stdin.readlines()]

    polymer: str = lines[0]

    rules: Dict[str, str] = {}
    for line in lines[2:]:
        rule_from, rule_to = line.split(' -> ')
        rules[rule_from] = rule_to

    return polymer, rules


def process_polymer(polymer: str, rules: Dict[str, str], steps: int) -> int:

    def extend_polymer(polymer: str, rules: Dict[str, str]) -> str:
        polymer_new: str = ''
        for idx, polymer_char in enumerate(polymer):
            polymer_new += polymer_char

            if idx + 2 <= len(polymer):
                rule_from = polymer[idx:idx + 2]
                if rule_from in rules:
                    polymer_new += rules[rule_from]

        return polymer_new

    for _ in range(steps):
        polymer = extend_polymer(polymer, rules)

    element_count: DefaultDict[str, int] = defaultdict(int)
    for element in polymer:
        element_count[element] += 1

    most_common_element = max(element_count.values())
    least_common_element = min(element_count.values())
    return most_common_element - least_common_element


if __name__ == '__main__':
    polymer, rules = read_input()
    print(f'Part 1: {process_polymer(polymer, rules, 10)}')
