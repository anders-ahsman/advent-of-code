import sys
from collections import defaultdict
from enum import Enum
from intcode_computer import IntcodeComputer

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program):
    pos = (0, 0)
    direction = Direction.UP
    painted = defaultdict(int)
    painted[pos] = 1

    computer = IntcodeComputer(program)
    com_iter = computer.run()
    try:
        while True:
            computer.inputs.append(painted[pos])

            color = next(com_iter)
            painted[pos] = color

            turn_dir = next(com_iter)
            direction = turn(direction, turn_dir)
            pos = move(pos, direction)
    except StopIteration:
        pass

    for y in range(20):
        for x in range(80):
            pos = (x, y)
            value = '#' if pos in painted and painted[pos] == 1 else ' '
            print(value, end='')
        print()

def turn(direction, turn_dir):
    if turn_dir == 0: # left 90 deg
        if direction == Direction.UP:
            direction = Direction.LEFT
        elif direction == Direction.LEFT:
            direction = Direction.DOWN
        elif direction == Direction.DOWN:
            direction = Direction.RIGHT
        elif direction == Direction.RIGHT:
            direction = Direction.UP
    elif turn_dir == 1 : # right 90 deg
        if direction == Direction.UP:
            direction = Direction.RIGHT
        elif direction == Direction.RIGHT:
            direction = Direction.DOWN
        elif direction == Direction.DOWN:
            direction = Direction.LEFT
        elif direction == Direction.LEFT:
            direction = Direction.UP
    else:
        raise Exception(f'Unknown turn direction {turn_dir}')

    return direction

def move(pos, direction):
    if direction == Direction.UP:
        pos = (pos[0], pos[1] - 1)
    elif direction == Direction.LEFT:
        pos = (pos[0] - 1, pos[1])
    elif direction == Direction.DOWN:
        pos = (pos[0], pos[1] + 1)
    elif direction == Direction.RIGHT:
        pos = (pos[0] + 1, pos[1])
    else:
        raise Exception(f'Unknown direction {direction}')

    return pos

if __name__ == '__main__':
    program = read_input()
    main(program)
