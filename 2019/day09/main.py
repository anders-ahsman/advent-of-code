import sys
from intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program):
    c1 = IntcodeComputer(program)
    c1.inputs.append(1)
    print(f'part1: {c1.run()}')

    c2 = IntcodeComputer(program)
    c2.inputs.append(2)
    print(f'part2: {c2.run()}')

if __name__ == '__main__':
    program = read_input()
    main(program)
