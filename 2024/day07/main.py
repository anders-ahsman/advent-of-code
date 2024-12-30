#!/usr/bin/env python3

import itertools
import operator
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Equation:
    test_value: int
    numbers: list[int]


def read_input() -> list[Equation]:
    equations: list[Equation] = []
    for line in sys.stdin:
        answer, numbers = line.strip().split(': ')
        equations.append(Equation(int(answer), [int(n) for n in numbers.split()]))

    return equations


def part1(equations: list[Equation]) -> int:
    operators = [operator.add, operator.mul]
    sum_test_values = 0
    for equation in equations:
        for op_combo in itertools.product(operators, repeat=len(equation.numbers) - 1):
            result = equation.numbers[0]
            for i in range(1, len(equation.numbers)):
                result = op_combo[i - 1](result, equation.numbers[i])

            if result == equation.test_value:
                sum_test_values += result
                break

    return sum_test_values


if __name__ == '__main__':
    equations = read_input()
    print(f'Part 1: {part1(equations)}')
