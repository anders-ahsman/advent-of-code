import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    computer.program[1] = 12
    computer.program[2] = 2
    it = computer.run()
    try:
        while True:
            next(it)
    except StopIteration:
        output = computer.program[0]
        print(f'part1: {output}')

def part2(program):
    expected = 19690720
    for noun in range(100):
        for verb in range(100):
            computer = IntcodeComputer(program)
            computer.program[1] = noun
            computer.program[2] = verb
            it = computer.run()

            try:
                while True:
                    next(it)
            except StopIteration:
                output = computer.program[0]
                if output == expected:
                    print(f'part2: {100 * noun + verb}')

if __name__ == '__main__':
    program = read_input()
    part1(program)
    part2(program)