import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1_and_2(program):
    computer_count = 50
    computers = []
    iters = []

    for i in range(computer_count):
        c = IntcodeComputer(program)
        c.inputs.append(i)
        computers.append(c)
        iters.append(c.run())

    first_y_sent_from_nat = None
    y_sent_from_nat = set()
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
                        if not first_y_sent_from_nat:
                            first_y_sent_from_nat = y
                        if all(not c1.inputs for c1 in computers):
                            if y in y_sent_from_nat:
                                print(f'Part 1: {first_y_sent_from_nat}')
                                print(f'Part 2: {y}')
                                return
                            computers[0].inputs.extend([x, y])
                            y_sent_from_nat.add(y)
                    else:
                        computers[a].inputs.extend([x, y])
                except IndexError: # No input available
                    iters[i] = c.run() # Retry same instruction next iteration for computer (input will be provied)
                    break

if __name__ == '__main__':
    program = read_input()
    part1_and_2(program)