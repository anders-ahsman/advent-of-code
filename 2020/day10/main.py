from collections import defaultdict
import sys


def read_jolts():
    return [int(line.rstrip()) for line in sys.stdin]


def part1(jolts):
    jolts = sorted(jolts + [0, max(jolts) + 3])
    diff1_count = sum(1 for a, b in zip(jolts, jolts[1:]) if b - a == 1)
    diff3_count = sum(1 for a, b in zip(jolts, jolts[1:]) if b - a == 3)
    return diff1_count * diff3_count


def part2(jolts):
    jolts = sorted(jolts + [0, max(jolts) + 3])
    connected_count = defaultdict(int)
    length = 1
    for jolt, last_jolt in zip(jolts[1:], jolts):
        if jolt - last_jolt == 1:
            length += 1
        else:
            if length > 2:
                connected_count[length] += 1
            length = 1
    res = 1
    factors = {3: 2, 4: 4, 5: 7}
    for length, count in connected_count.items():
        res *= factors[length] ** count
    return res


if __name__ == '__main__':
    jolts = read_jolts()
    print(f'Part 1: {part1(jolts)}')
    print(f'Part 2: {part2(jolts)}')
