import sys

def read_input():
    opcodes = [int(x) for x in next(sys.stdin).split(',')]
    return opcodes

def main(opcodes):
    opcodes_copy = opcodes[:]
    pos = 0
    for noun in range(100):
        for verb in range(100):
            opcodes[1] = noun
            opcodes[2] = verb

            while True:
                op = opcodes[pos]
                if op == 1:
                    opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] + opcodes[opcodes[pos + 2]]
                elif op == 2:
                    opcodes[opcodes[pos + 3]] = opcodes[opcodes[pos + 1]] * opcodes[opcodes[pos + 2]]
                elif op == 99:
                    break

                pos += 4

            if opcodes[0] == 19690720:
                return noun, verb
            else:
                opcodes = opcodes_copy[:]
                pos = 0

if __name__ == '__main__':
    opcodes = read_input()
    noun, verb = main(opcodes)
    print('100 * noun + verb:', 100 * noun + verb)