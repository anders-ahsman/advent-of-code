import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    limit = 50
    space = scan_space(program, limit)

    for y in range(limit):
        for x in range(limit):
            if (x, y) in space:
                print('#' if space[(x, y)] == 1 else '.', end='')
            else:
                print('?', end='')
        print()

    beam_point_count = sum([1 for beam in space.values() if beam == 1])
    print('Part 1:', beam_point_count)

def scan_space(program, limit):
    space = {}
    x = 0
    y = 0
    prev_output_for_row = None
    while y < limit:
        computer = IntcodeComputer(program)
        it = computer.run()

        try:
            computer.inputs.append(x)
            computer.inputs.append(y)
            output = next(it)
            space[(x, y)] = output

            end_of_beam_for_row = output == 0 and prev_output_for_row == 1
            if end_of_beam_for_row:
                beam_start_for_row = min([pos[0] for pos, beam in space.items() if beam and pos[1] == y])
                x = beam_start_for_row - 1
                y += 1
                prev_output_for_row = None
            else:
                prev_output_for_row = output
                x += 1
                if x == limit:
                    x = 0
                    y += 1
                    prev_output_for_row = None
        except StopIteration:
            pass

    return space

if __name__ == '__main__':
    program = read_input()
    part1(program)
