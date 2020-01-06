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
        'OR A J',
        'AND B J',
        'AND C J',
        'NOT J J',
        'AND D J',
        'WALK']
    for instruction in instructions:
        for char in instruction:
            computer.inputs.append(ord(char))
        computer.inputs.append(10)

    run_until_stop(it)

def part2(program):
    computer = IntcodeComputer(program)
    it = computer.run()

    # (!(A and B and C) and D) and (E or H)
    instructions = [
        'OR A J',
        'AND B J',
        'AND C J',
        'NOT J J',
        'AND D J',
        'OR E T',
        'OR H T',
        'AND T J',
        'RUN']
    for instruction in instructions:
        for char in instruction:
            computer.inputs.append(ord(char))
        computer.inputs.append(10)

    run_until_stop(it)

def run_until_stop(it):
    while True:
        try:
            output = next(it)
            if output < 255:
                print(chr(output), end='')
            else:
                print(output)
        except StopIteration:
            print()
            break

program = read_input()
part1(program)
part2(program)