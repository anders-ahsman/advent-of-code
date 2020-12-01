from itertools import combinations
import sys


def read_input():
    return [int(number) for number in sys.stdin]


def find_multiple(numbers, target):
    for (a, b) in combinations(numbers, 2):
        if a + b == target:
            return a * b


def find_multiple2(numbers, target):
    for (a, b, c) in combinations(numbers, 3):
        if a + b + c == target:
            return a * b * c


if __name__ == '__main__':
    numbers = read_input()
    target = 2020
    print(f'Part 1: {find_multiple(numbers, target)}')
    print(f'Part 2: {find_multiple2(numbers, target)}')
