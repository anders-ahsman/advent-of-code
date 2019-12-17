import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    it = computer.run()
    rows = get_camera_feed(it)

    intersections = set()
    scaffold = ord('#')
    for y, line in enumerate(rows):
        for x, char in enumerate(line):
            try:
                if char == scaffold and \
                    line[x-1]    == scaffold and line[x+1]    == scaffold and \
                    rows[y-1][x] == scaffold and rows[y+1][x] == scaffold:
                        intersections.add((x, y))
            except IndexError:
                pass

    print(f'Part 1: {sum([x * y for x, y in intersections])}')

def get_camera_feed(it):
    rows = []
    line = []
    try:
        while True:
            output = next(it)
            if output == 10:
                rows.append(line)
                line = []
            else:
                line.append(output)
    except StopIteration:
        pass
    return rows

if __name__ == '__main__':
    program = read_input()
    part1(program)
