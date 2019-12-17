import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    it = computer.run()

    try:
        rows = []
        line = []
        while True:
            output = next(it)
            if output == 10:
                rows.append(line)
                line = []
            else:
                line.append(output)

            print(chr(output), end='')
    except StopIteration:
        pass

    intersections = set()
    for y, line in enumerate(rows):
        for x, char in enumerate(line):
            try:
                if char == 35 and line[x-1] == 35 and line[x+1] == 35 and rows[y-1][x] == 35 and rows[y+1][x] == 35:
                    intersections.add((x, y))
            except IndexError:
                pass

    print(sum([x * y for x, y in intersections]))

if __name__ == '__main__':
    program = read_input()
    part1(program)
