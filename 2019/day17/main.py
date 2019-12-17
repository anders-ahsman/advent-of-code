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

def part2(program):
    program[0] = 2
    computer = IntcodeComputer(program)
    computer.inputs = get_movement_pattern()
    it = computer.run()
    try:
        while True:
            output = next(it)
            if output == 10:
                print()
            elif output > 255:
                print(output)
            else:
                print(chr(output), end='')
    except StopIteration:
        pass

def get_movement_pattern():
    movement_pattern = []
    for command in ['A,B,A,C', 'R,10', 'L,8', 'R,4,L,6', 'n']:
        for part in command.split(','):
            for char in part:
                movement_pattern.append(ord(char))
            movement_pattern.append(ord(','))
        movement_pattern.pop() # remove last ','
        movement_pattern.append(ord('\n'))
    return movement_pattern

if __name__ == '__main__':
    program = read_input()
    # part1(program)
    part2(program)