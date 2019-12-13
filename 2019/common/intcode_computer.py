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
        self.idx = 0
        self.relative_base = 0
        self.inputs = []
        self.program = defaultdict(int)
        for i, op in enumerate(program):
            self.program[i] = op

    def run(self):
        while True:
            opcode = self.program[self.idx]
            mode1, mode2, mode3 = self.get_modes(opcode)
            instruction = Instruction(int(str(opcode)[-2:]))

            if instruction == Instruction.ADD:
                param1, param2 = self.get_params(mode1, mode2)
                result = param1 + param2

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.idx + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.idx + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.idx + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')
                self.idx += 4

            elif instruction == Instruction.MULTIPLY:
                param1, param2 = self.get_params(mode1, mode2)
                result = param1 * param2

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.idx + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.idx + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.idx + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')
                self.idx += 4

            elif instruction == Instruction.INPUT:
                indata = self.inputs[0]
                self.inputs = self.inputs[1:]

                if mode1 == Mode.POSITION:
                    self.program[self.program[self.idx + 1]] = indata
                elif mode1 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.idx + 1]] = indata
                else:
                    raise Exception(f'Unknown mode {mode1}')
                self.idx += 2

            elif instruction == Instruction.OUTPUT:
                yield self.get_param(mode1, 1)
                self.idx += 2

            elif instruction == Instruction.JUMP_IF_TRUE:
                param1, param2 = self.get_params(mode1, mode2)
                self.idx = param2 if param1 else self.idx + 3

            elif instruction == Instruction.JUMP_IF_FALSE:
                param1, param2 = self.get_params(mode1, mode2)
                self.idx = param2 if not param1 else self.idx + 3

            elif instruction == Instruction.LESS_THAN:
                param1, param2 = self.get_params(mode1, mode2)
                result = int(param1 < param2)

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.idx + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.idx + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.idx + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')
                self.idx += 4

            elif instruction == Instruction.EQUALS:
                param1, param2 = self.get_params(mode1, mode2)
                result = int(param1 == param2)

                if mode3 == Mode.POSITION:
                    self.program[self.program[self.idx + 3]] = result
                elif mode3 == Mode.IMMEDIATE:
                    self.program[self.idx + 3] = result
                elif mode3 == Mode.RELATIVE:
                    self.program[self.relative_base + self.program[self.idx + 3]] = result
                else:
                    raise Exception(f'Unknown mode {mode3}')
                self.idx += 4

            elif instruction == Instruction.ADJUST_RELATIVE_BASE:
                param1 = self.get_param(mode1, 1)
                self.relative_base += param1
                self.idx += 2

            elif instruction == Instruction.ABORT:
                return

            else:
                raise Exception(f'Unknown instruction {instruction}')

    def get_modes(self, opcode):
        modes = [int(m) for m in list(f'{opcode:05}'[:3])]
        mode1 = Mode(modes.pop())
        mode2 = Mode(modes.pop())
        mode3 = Mode(modes.pop())
        return mode1, mode2, mode3

    def get_params(self, mode1, mode2):
        return self.get_param(mode1, 1), self.get_param(mode2, 2)

    def get_param(self, mode, offset):
        if mode == Mode.POSITION:
            return self.program[self.program[self.idx + offset]]
        elif mode == Mode.IMMEDIATE:
            return self.program[self.idx + offset]
        elif mode == Mode.RELATIVE:
            return self.program[self.relative_base + self.program[self.idx + offset]]

        raise Exception(f'Unknown mode {mode}')