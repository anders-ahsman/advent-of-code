from enum import Enum
from itertools import permutations
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

class IntcodeComputer:
    def __init__(self, program):
        self.program = program[:]

    def run(self, inputs):
        self.pos = 0
        self.output = None
        inputs.reverse()

        while True:
            opcode = self.program[self.pos]

            mode_1st_param, mode_2nd_param, mode_3rd_param = self.set_modes(opcode)

            opcode = int(str(opcode)[-2:])
            if opcode == Instruction.ADD.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                result = val1 + val2

                if mode_3rd_param == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode_3rd_param == Mode.POSITION:
                    self.program[self.pos + 3] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')

                self.pos += 4

            elif opcode == Instruction.MULTIPLY.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                result = val1 * val2

                if mode_3rd_param == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode_3rd_param == Mode.POSITION:
                    self.program[self.pos + 3] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')
                self.pos += 4

            elif opcode == Instruction.INPUT.value:
                self.program[self.program[self.pos + 1]] = inputs.pop()
                self.pos += 2

            elif opcode == Instruction.OUTPUT.value:
                self.output = self.program[self.program[self.pos + 1]]
                self.pos += 2

            elif opcode == Instruction.JUMP_IF_TRUE.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                self.pos = val2 if val1 else self.pos + 3

            elif opcode == Instruction.JUMP_IF_FALSE.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                self.pos = val2 if not val1 else self.pos + 3

            elif opcode == Instruction.LESS_THAN.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                result = 1 if val1 < val2 else 0

                if mode_3rd_param == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode_3rd_param == Mode.POSITION:
                    self.program[self.pos + 3] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')

                self.pos += 4

            elif opcode == Instruction.EQUALS.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                result = 1 if val1 == val2 else 0

                if mode_3rd_param == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode_3rd_param == Mode.POSITION:
                    self.program[self.pos + 3] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')

                self.pos += 4

            elif opcode == Instruction.ABORT.value:
                return self.output

            else:
                raise Exception(f'Unknown opcode {opcode}')

    def set_modes(self, opcode):
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

        return mode_1st_param, mode_2nd_param, mode_3rd_param

    def get_param(self, offset, mode):
        if mode == Mode.POSITION:
            return self.program[self.program[self.pos + offset]]
        elif mode == Mode.IMMEDIATE:
            return self.program[self.pos + offset]

        raise Exception(f'Unknown mode {mode}')

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program):
    computers = []
    for _ in range(5):
        computers.append(IntcodeComputer(program))

    max_output = 0
    for phases in [''.join(p) for p in permutations('01234')]:
        phases = [int(p) for p in list(phases)]
        last_output = None
        for i, phase in enumerate(phases):
            c = IntcodeComputer(program)
            inputs = list((phase, last_output if i > 0 else 0))
            last_output = c.run(inputs)
            if last_output > max_output:
                max_output = last_output

    print(f'max_output {max_output}')


if __name__ == '__main__':
    program = read_input()
    main(program)
