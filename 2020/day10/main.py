import sys


def read_jolts():
    return [int(line.rstrip()) for line in sys.stdin]


def part1(jolts):
    diff1_count = 0
    diff3_count = 0
    for i in range(1, len(jolts)):
        jolt = jolts[i]
        last_jolt = jolts[i - 1]
        if jolt == last_jolt + 1:
            diff1_count +=1
        elif jolt == last_jolt + 3:
            diff3_count += 1
        else:
            raise ValueError(jolt, last_jolt)
    return diff1_count * diff3_count


if __name__ == '__main__':
    jolts = read_jolts()
    jolts += [0, max(jolts) + 3]
    jolts = sorted(jolts)

    print(f'Part 1: {part1(jolts)}')
