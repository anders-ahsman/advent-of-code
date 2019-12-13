import sys
from enum import Enum

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    it = computer.run()

    try:
        block_count = 0
        while True:
            x, y, tile = next(it), next(it), Tile(next(it))
            if tile == Tile.BLOCK:
                block_count += 1
    except StopIteration:
        pass

    print(f'part1: {block_count}')

if __name__ == '__main__':
    program = read_input()
    part1(program)
