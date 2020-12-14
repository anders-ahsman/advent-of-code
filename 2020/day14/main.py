from collections import defaultdict
from itertools import product
import re
import sys


def read_input():
    return [line.rstrip() for line in sys.stdin]


def part1(lines):
    mem = defaultdict(lambda: ['0'] * 36)
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
    s = sum(int(''.join(mem[addr]), 2) for addr in mem)
    return s


def part2(lines):
    def update(mem, addr_bin, value):
        addr = int(''.join(addr_bin), 2)
        mem[addr] = list(f'{value:036b}')

    mem = defaultdict(lambda: ['0'] * 36)
    mask = '0' * 36
    for line in lines:
        if 'mask' in line:
            mask = line.split('mask = ')[1]
        else:
            m = re.match(r'^mem\[(\d+)\] = (\d+)$', line)
            addr = int(m[1])
            addr_bin = list(f'{addr:036b}')
            value = int(m[2])
            for bitcombo in product(range(2), repeat=mask.count('X')):
                # e.g. repeat=3 --> 000 001 010 011 100 101 110 111
                bitcombo = iter(bitcombo)
                for i, bit in enumerate(mask):
                    if bit == '1':
                        addr_bin[i] = '1'
                    elif bit == 'X':
                        addr_bin[i] = str(next(bitcombo))
                update(mem, addr_bin, value)
    s = sum(int(''.join(mem[addr]), 2) for addr in mem)
    return s


if __name__ == '__main__':
    lines = read_input()
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
