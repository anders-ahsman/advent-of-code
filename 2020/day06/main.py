import string
import sys


def read_lines():
    return [line.strip() for line in sys.stdin]


def part1(lines):
    groups = []
    answers = set()
    for line in lines:
        if len(line) > 0:
            for ch in line:
                answers.add(ch)
        else:
            groups.append(answers)
            answers = set()
    groups.append(answers)

    anyone_yes_sum = sum(len(group) for group in groups)
    return anyone_yes_sum


def part2(lines):
    groups = []
    answers = []
    for line in lines:
        if len(line) > 0:
            answers.append(line)
        else:
            groups.append(answers)
            answers = []
    groups.append(answers)

    everybody_yes_sum = 0
    for group in groups:
        for letter in string.ascii_lowercase:
            if all(letter in answer for answer in group):
                everybody_yes_sum += 1
    return everybody_yes_sum


if __name__ == '__main__':
    lines = read_lines()
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
