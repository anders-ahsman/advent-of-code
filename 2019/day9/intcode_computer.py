from collections import defaultdict
from enum import Enum
from itertools import permutations

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
            mode1, mode2, mode3 = self.get_modes(opcode)

            opcode = int(str(opcode)[-2:])
            if opcode == Instruction.ADD.value:
                val1 = self.get_param(1, mode1)
                val2 = self.get_param(2, mode2)
                result = val1 + val2

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')

                self.pos += 4

            elif opcode == Instruction.MULTIPLY.value:
                val1 = self.get_param(1, mode1)
                val2 = self.get_param(2, mode2)
                result = val1 * val2

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')
                self.pos += 4

            elif opcode == Instruction.INPUT.value:
                indata = self.inputs[0]
                self.inputs = self.inputs[1:]

                if mode1 == Mode.POSITION:
                    self.program[self.program[self.pos + 1]] = indata
                elif mode1 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 1]] = indata
                else:
                    raise Exception(f'Unknown mode {mode1}')

                self.pos += 2

            elif opcode == Instruction.OUTPUT.value:
                self.output = self.get_param(1, mode1)
                self.pos += 2

            elif opcode == Instruction.JUMP_IF_TRUE.value:
                val1 = self.get_param(1, mode1)
                val2 = self.get_param(2, mode2)
                self.pos = val2 if val1 else self.pos + 3

            elif opcode == Instruction.JUMP_IF_FALSE.value:
                val1 = self.get_param(1, mode1)
                val2 = self.get_param(2, mode2)
                self.pos = val2 if not val1 else self.pos + 3

            elif opcode == Instruction.LESS_THAN.value:
                val1 = self.get_param(1, mode1)
                val2 = self.get_param(2, mode2)
                result = 1 if val1 < val2 else 0

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')

                self.pos += 4

            elif opcode == Instruction.EQUALS.value:
                val1 = self.get_param(1, mode1)
                val2 = self.get_param(2, mode2)
                result = 1 if val1 == val2 else 0

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.pos + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.pos + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.pos + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')

                self.pos += 4

            elif opcode == Instruction.ADJUST_RELATIVE_BASE.value:
                val1 = self.get_param(1, mode1)
                self.relative_base += val1
                self.pos += 2

            elif opcode == Instruction.ABORT.value:
                return self.output

            else:
                raise Exception(f'Unknown opcode {opcode}')

    def get_modes(self, opcode):
        if len(str(opcode)) > 2:
            modes_raw = list([int(x) for x in str(opcode)[:-2]])

            try:
                mode1 = Mode(modes_raw.pop())
            except IndexError:
                mode1 = Mode.POSITION

            try:
                mode2 = Mode(modes_raw.pop())
            except IndexError:
                mode2 = Mode.POSITION

            try:
                mode3 = Mode(modes_raw.pop())
            except IndexError:
                mode3 = Mode.POSITION
        else:
            mode1 = Mode.POSITION
            mode2 = Mode.POSITION
            mode3 = Mode.POSITION

        return mode1, mode2, mode3

    def get_param(self, offset, mode):
        if mode == Mode.POSITION:
            return self.program[self.program[self.pos + offset]]
        elif mode == Mode.IMMEDIATE:
            return self.program[self.pos + offset]
        elif mode == Mode.RELATIVE:
            return self.program[self.relative_base + self.program[self.pos + offset]]

        raise Exception(f'Unknown mode {mode}')