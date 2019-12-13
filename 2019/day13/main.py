import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program):
    computer = IntcodeComputer(program)
    it = computer.run()
    try:
        block_count = 0
        while True:
            x, y, output = next(it), next(it), next(it)
            if output == 2:
                block_count += 1
    except StopIteration:
        pass

    print(block_count)

if __name__ == '__main__':
    program = read_input()
    main(program)
