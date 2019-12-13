import curses
import sys
from time import sleep
from enum import Enum

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def part1(program):
    computer = IntcodeComputer(program)
    it = computer.run()

    try:
        block_count = 0
        while True:
            _, _, tile = next(it), next(it), Tile(next(it))
            if tile == Tile.BLOCK:
                block_count += 1
    except StopIteration:
        pass

    print(f'part1: {block_count}')

def part2(program):
    curses.wrapper(game, program)

def game(screen, program):
    curses.curs_set(False)

    program[0] = 2
    computer = IntcodeComputer(program)
    it = computer.run()

    try:
        count = 0
        ball_x = None
        paddle_x = None

        while True:
            x, y, output = next(it), next(it), next(it)

            if x == -1 and y == 0:
                screen.addstr(21, 0, f'Score: {output}')
            else:
                tile = Tile(output)
                if tile == Tile.EMPTY:
                    char = ' '
                elif tile == Tile.WALL:
                    char = '#'
                elif tile == Tile.BLOCK:
                    char = '@'
                elif tile == Tile.PADDLE:
                    char = '='
                    paddle_x = x
                elif tile == Tile.BALL:
                    char = '.'
                    ball_x = x
                screen.addstr(y, x, char)

                if ball_x is not None and paddle_x is not None:
                    if paddle_x < ball_x:
                        joystick = 1
                    elif paddle_x > ball_x:
                        joystick = -1
                    else:
                        joystick = 0
                    computer.inputs = [joystick]

            screen.refresh()
            sleep(0 if count < 760 else 0.01)
            count += 1

    except StopIteration:
        pass

if __name__ == '__main__':
    program = read_input()
    # part1(program)
    part2(program)
