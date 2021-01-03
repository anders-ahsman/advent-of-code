from collections import defaultdict
import sys


def read_input():
    return [line.rstrip() for line in sys.stdin]


def solve(lines, compare_func):
    word = ''
    letter_to_count = defaultdict(int)
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            ch = lines[j][i]
            letter_to_count[ch] += 1
        word += compare_func(letter_to_count)
        letter_to_count.clear()
    return word


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {solve(lines, lambda count: max(count, key=count.get))}')
    print(f'Part 2: {solve(lines, lambda count: min(count, key=count.get))}')
