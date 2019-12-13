from itertools import permutations
import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program, perms):
    max_output = 0
    for phases in [''.join(p) for p in permutations(perms)]:
        phases = [int(p) for p in list(phases)]
        is_first_instruction = True
        computers = []
        computers_to_iters = {}
        for phase in phases:
            c = IntcodeComputer(program)
            c.inputs.append(phase)
            computers.append(c)
            computers_to_iters[c] = c.run()
        try:
            while True:
                for i, phase in enumerate(phases):
                    c = computers[i]
                    c.inputs.append(0 if is_first_instruction else last_output)
                    is_first_instruction = False

                    last_output = next(computers_to_iters[c])
                    max_output = max(last_output, max_output)
        except StopIteration:
            pass

    print(max_output)

if __name__ == '__main__':
    program = read_input()
    main(program, '01234')
    main(program, '56789')
