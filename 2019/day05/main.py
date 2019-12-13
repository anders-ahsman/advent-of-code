import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program, indata):
    computer = IntcodeComputer(program)
    computer.inputs.append(indata)
    it = computer.run()

    last_output = None
    try:
        while True:
            last_output = next(it)
    except StopIteration:
        print(last_output)

if __name__ == '__main__':
    program = read_input()
    main(program, 1)
    main(program, 5)