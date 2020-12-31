import sys


def read_jolts():
    return [int(line.rstrip()) for line in sys.stdin]


def part1(jolts):
    jolts += [0, max(jolts) + 3]
    jolts = sorted(jolts)
    diff1_count = sum(1 for a, b in zip(jolts, jolts[1:]) if b - a == 1)
    diff3_count = sum(1 for a, b in zip(jolts, jolts[1:]) if b - a == 3)
    return diff1_count * diff3_count


if __name__ == '__main__':
    jolts = read_jolts()
    print(f'Part 1: {part1(jolts)}')
