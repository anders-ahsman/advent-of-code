import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    it = computer.run()

    x = 0
    y = 0
    ones = 0
    while x < 50 and y < 50:
        try:
            # print(x,y)
            computer = IntcodeComputer(program)
            it = computer.run()
            computer.inputs.append(x)
            computer.inputs.append(y)
            x += 1
            if (x == 50):
                x = 0
                y += 1
            output = next(it)
            if output == 1:
                ones += 1

        except StopIteration:
            pass

    print(ones)
    # rows = get_camera_feed(it)

    # intersections = set()
    # scaffold = ord('#')
    # for y, line in enumerate(rows):
    #     for x, char in enumerate(line):
    #         try:
    #             if char == scaffold and \
    #                 line[x-1]    == scaffold and line[x+1]    == scaffold and \
    #                 rows[y-1][x] == scaffold and rows[y+1][x] == scaffold:
    #                     intersections.add((x, y))
    #         except IndexError:
    #             pass

    # print(f'Part 1: {sum([x * y for x, y in intersections])}')


if __name__ == '__main__':
    program = read_input()
    part1(program)
