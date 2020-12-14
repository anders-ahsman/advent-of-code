import re
import sys


def read_input():
    return [line.rstrip() for line in sys.stdin]


def part1(lines):
    mem = []
    for _ in range(99999):
        mem.append(['0'] * 36)
    mask = ['0' * 36]
    for line in lines:
        if 'mask' in line:
            mask = line.split('mask = ')[1]
        else:
            m = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
            address = int(m[1])
            value = int(m[2])
            value_bin = list(f'{value:036b}')
            for i, bit in enumerate(mask):
                mem[address][i] = bit if bit in ['0', '1'] else value_bin[i]
    s = sum(int(''.join(address), 2) for address in mem)
    return s


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {part1(lines)}')
