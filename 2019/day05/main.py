from enum import Enum
import sys

class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1

class Instruction(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ABORT = 99

def read_input():
    opcodes = [int(x) for x in next(sys.stdin).split(',')]
    return opcodes

def main(opcodes, indata):
    pos = 0
    outdata = None

    while True:
        opcode = opcodes[pos]
        mode_1st_param, mode_2nd_param, mode_3rd_param = set_modes(opcode)

        opcode = int(str(opcode)[-2:])
        if opcode == Instruction.ADD.value:
            val1 = get_param(opcodes, pos + 1, mode_1st_param)
            val2 = get_param(opcodes, pos + 2, mode_2nd_param)
            result = val1 + val2

            if mode_3rd_param == Mode.POSITION:
                opcodes[opcodes[pos + 3]] = result
            else:
                opcodes[pos + 3] = result

            pos += 4

        elif opcode == Instruction.MULTIPLY.value:
            val1 = get_param(opcodes, pos + 1, mode_1st_param)
            val2 = get_param(opcodes, pos + 2, mode_2nd_param)
            result = val1 * val2

            if mode_3rd_param == Mode.POSITION:
                opcodes[opcodes[pos + 3]] = result
            else:
                opcodes[pos + 3] = result
            pos += 4

        elif opcode == Instruction.INPUT.value:
            opcodes[opcodes[pos + 1]] = indata
            pos += 2

        elif opcode == Instruction.OUTPUT.value:
            outdata = opcodes[opcodes[pos + 1]]
            pos += 2

        elif opcode == Instruction.JUMP_IF_TRUE.value:
            val1 = get_param(opcodes, pos + 1, mode_1st_param)
            val2 = get_param(opcodes, pos + 2, mode_2nd_param)
            pos = val2 if val1 else pos + 3

        elif opcode == Instruction.JUMP_IF_FALSE.value:
            val1 = get_param(opcodes, pos + 1, mode_1st_param)
            val2 = get_param(opcodes, pos + 2, mode_2nd_param)
            pos = val2 if not val1 else pos + 3

        elif opcode == Instruction.LESS_THAN.value:
            val1 = get_param(opcodes, pos + 1, mode_1st_param)
            val2 = get_param(opcodes, pos + 2, mode_2nd_param)
            result = 1 if val1 < val2 else 0

            if mode_3rd_param == Mode.POSITION:
                opcodes[opcodes[pos + 3]] = result
            else:
                opcodes[pos + 3] = result

            pos += 4

        elif opcode == Instruction.EQUALS.value:
            val1 = get_param(opcodes, pos + 1, mode_1st_param)
            val2 = get_param(opcodes, pos + 2, mode_2nd_param)
            result = 1 if val1 == val2 else 0

            if mode_3rd_param == Mode.POSITION:
                opcodes[opcodes[pos + 3]] = result
            else:
                opcodes[pos + 3] = result

            pos += 4

        elif opcode == Instruction.ABORT.value:
            return outdata

        else:
            raise Exception(f'Unknown opcode {opcode}')

def set_modes(opcode):
    if len(str(opcode)) > 2:
        modes = str(opcode)[:-2]

        try:
            mode_1st_param = Mode(int(modes[-1:]))
        except ValueError:
            mode_1st_param = Mode.POSITION
        modes = modes[:-1]

        try:
            mode_2nd_param = Mode(int(modes[-1:]))
        except ValueError:
            mode_2nd_param = Mode.POSITION
        modes = modes[:-1]

        try:
            mode_3rd_param = Mode(int(modes[-1:]))
        except ValueError:
            mode_3rd_param = Mode.POSITION
    else:
        mode_1st_param = Mode.POSITION
        mode_2nd_param = Mode.POSITION
        mode_3rd_param = Mode.POSITION

    return (mode_1st_param, mode_2nd_param, mode_3rd_param)

def get_param(opcodes, pos, mode):
    if mode == Mode.POSITION:
        return opcodes[opcodes[pos]]
    elif mode == Mode.IMMEDIATE:
        return opcodes[pos]

    raise Exception(f'Unknown mode {mode}')

if __name__ == '__main__':
    opcodes = read_input()

    print(main(opcodes[:], 1))
    print(main(opcodes[:], 5))