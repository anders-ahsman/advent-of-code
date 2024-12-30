#!/usr/bin/env python3

import itertools
import operator
import sys
from dataclasses import dataclass
from typing import Callable

BinaryIntOp = Callable[[int, int], int]


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
    return calculate_test_value_sum(equations, operators)


def part2(equations: list[Equation]) -> int:
    def concat(a: int, b: int) -> int:
        return int(str(a) + str(b))

    operators = [operator.add, operator.mul, concat]
    return calculate_test_value_sum(equations, operators)


def calculate_test_value_sum(equations: list[Equation], operators: list[BinaryIntOp]) -> int:
    test_value_sum = 0
    for equation in equations:
        for op_combo in itertools.product(operators, repeat=len(equation.numbers) - 1):
            result = equation.numbers[0]
            for i in range(1, len(equation.numbers)):
                result = op_combo[i - 1](result, equation.numbers[i])

            if result == equation.test_value:
                test_value_sum += result
                break

    return test_value_sum


if __name__ == '__main__':
    equations = read_input()
    print(f'Part 1: {part1(equations)}')
    print(f'Part 2: {part2(equations)}')
