from itertools import combinations
import sys


def read_numbers():
    return [int(line.rstrip()) for line in sys.stdin]


def part1(numbers):
    current, incoming = numbers[:25], numbers[25:]
    while len(incoming) > 0:
        next_number = incoming[0]
        if not any(sum(combination) == next_number for combination in combinations(current, 2)):
            return next_number
        current = current[1:] + [next_number]
        incoming = incoming[1:]


def part2(numbers, target):
    i = 0
    j = 0
    numbers_added = []
    while i < len(numbers):
        j = i
        while sum(numbers_added) < target:
            numbers_added.append(numbers[j])
            j += 1
        if sum(numbers_added) == target:
            return min(numbers_added) + max(numbers_added)
        i += 1
        numbers_added = []


if __name__ == '__main__':
    numbers = read_numbers()
    target = part1(numbers)
    print(f'Part 1: {target}')
    print(f'Part 2: {part2(numbers, target)}')
