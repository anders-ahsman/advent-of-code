import math
import sys

def read_input():
    opcodes = [int(x) for x in next(sys.stdin).split(',')]
    return opcodes

def main(opcodes):
    pos = 0
    while True:
        print(opcodes)

        op = opcodes[pos]
        if op == 1:
            opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] + opcodes[opcodes[pos + 2]]
        elif op == 2:
            opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] * opcodes[opcodes[pos + 2]]
        elif op == 99:
            return opcodes

        pos += 4

if __name__ == '__main__':
    opcodes = read_input()
    result = main(opcodes)
    print('result', result)