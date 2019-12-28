import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer_count = 50
    computers = []
    iters = []

    for i in range(computer_count):
        c = IntcodeComputer(program)
        c.inputs.append(i)
        computers.append(c)
        iters.append(c.run())

    while True:
        for i in range(computer_count):
            c = computers[i]
            it = iters[i]

            while True:
                if not c.inputs:
                    c.inputs.append(-1)
                try:
                    a, x, y = next(it), next(it), next(it)
                    if a == 255:
                        print(f'Part1: {y}')
                        return
                    computers[a].inputs.extend([x, y])
                except IndexError: # No input available
                    iters[i] = c.run() # Retry same instruction next iteration for computer (input will be provied)
                    break

if __name__ == '__main__':
    program = read_input()
    part1(program)