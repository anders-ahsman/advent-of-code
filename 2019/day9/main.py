from collections import defaultdict
from enum import Enum
from itertools import permutations
import sys

class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class Instruction(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_RELATIVE_BASE = 9
    ABORT = 99

class IntcodeComputer:
    def __init__(self, program):
        self.pos = 0
        self.relative_base = 0
        self.inputs = []
        self.output = None
        self.program = defaultdict(int)
        for i, op in enumerate(program):
            self.program[i] = op

    def run(self):
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
                elif mode_3rd_param == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode_3rd_param == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')

                self.pos += 4

            elif opcode == Instruction.MULTIPLY.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                result = val1 * val2

                if mode_3rd_param == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode_3rd_param == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode_3rd_param == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')
                self.pos += 4

            elif opcode == Instruction.INPUT.value:
                indata = self.inputs[0]
                self.inputs = self.inputs[1:]

                if mode_1st_param == Mode.POSITION:
                    self.program[self.program[self.pos + 1]] = indata
                elif mode_1st_param == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 1]] = indata
                else:
                    raise Exception(f'Unknown mode {mode_1st_param}')

                self.pos += 2

            elif opcode == Instruction.OUTPUT.value:
                self.output = self.get_param(1, mode_1st_param)
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
                elif mode_3rd_param == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode_3rd_param == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')

                self.pos += 4

            elif opcode == Instruction.EQUALS.value:
                val1 = self.get_param(1, mode_1st_param)
                val2 = self.get_param(2, mode_2nd_param)
                result = 1 if val1 == val2 else 0

                if mode_3rd_param == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode_3rd_param == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode_3rd_param == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode_3rd_param}')

                self.pos += 4

            elif opcode == Instruction.ADJUST_RELATIVE_BASE.value:
                val1 = self.get_param(1, mode_1st_param)
                self.relative_base += val1
                self.pos += 2

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
        elif mode == Mode.RELATIVE:
            return self.program[self.relative_base + self.program[self.pos + offset]]

        raise Exception(f'Unknown mode {mode}')

def read_input():
    program = [int(x) for x in next(sys.stdin).split(',')]
    return program

def main(program):
    c1 = IntcodeComputer(program)
    c1.inputs.append(1)
    print(f'part1: {c1.run()}')

    c2 = IntcodeComputer(program)
    c2.inputs.append(2)
    print(f'part2: {c2.run()}')

if __name__ == '__main__':
    program = read_input()
    main(program)
