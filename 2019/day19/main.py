import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    space = {}
    limit = 50
    x = 0
    y = 0
    last_output_for_row = None
    while y < limit:
        computer = IntcodeComputer(program)
        it = computer.run()

        try:
            computer.inputs.append(x)
            computer.inputs.append(y)
            output = next(it)
            space[(x, y)] = output

            end_of_beam_for_row = output == 0 and last_output_for_row == 1
            if end_of_beam_for_row:
                x = 0
                y += 1
                last_output_for_row = None
            else:
                last_output_for_row = output
                x += 1
                if x == limit:
                    x = 0
                    y += 1
                    last_output_for_row = None

        except StopIteration:
            pass

    ones = [v for v in space.values() if v == 1]
    print('Part 1:', len(ones))

if __name__ == '__main__':
    program = read_input()
    part1(program)
