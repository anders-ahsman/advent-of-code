import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input(filename):
    with open(filename, mode='r') as f:
        program = [int(x) for x in f.readline().split(',')]
    return program

def part1(program):
    com = IntcodeComputer(program)
    it = com.run()
    try:
        while True:
            line = read_line(it)
            print(line)
            if 'Command?' in line:
                cmd_str = input('') + '\n'
                com.inputs = [ord(ch) for ch in cmd_str]
    except StopIteration:
        pass

def read_line(it):
    line = []
    while True:
        output = next(it)
        if output == 10:
            break
        line.append(chr(output))
    return ''.join(ch for ch in line)

if __name__ == '__main__':
    filename = sys.argv[1]  # read from file, want to use stdin for keyboard
    program = read_input(filename)
    part1(program)
