import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    it = computer.run()

    # !(A and B and C) and D
    instructions = [
        'OR A T', # T starts out empty, copy A to T
        'AND B T',
        'AND C T',
        'NOT T J',
        'AND D J',
        'WALK']
    for instruction in instructions:
        for char in instruction:
            computer.inputs.append(ord(char))
        computer.inputs.append(10)

    while True:
        try:
            output = next(it)
            if output < 255:
                print(chr(output), end='')
            else:
                print(output)
        except StopIteration:
            break

program = read_input()
part1(program)