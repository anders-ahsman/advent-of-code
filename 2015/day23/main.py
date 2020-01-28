from collections import defaultdict
import sys
from typing import Dict, List


def run(instructions: List[str], registers: Dict[str, int]) -> Dict[str, int]:
    idx: int = 0
    while 0 <= idx < len(instructions):
        line: str = instructions[idx]
        instr: str = line[:3]
        args: str = line[4:]
        if instr == 'hlf':
            reg = args
            registers[reg] //= 2
            idx += 1
        elif instr == 'tpl':
            reg = args
            registers[reg] *= 3
            idx += 1
        elif instr == 'inc':
            reg = args
            registers[reg] += 1
            idx += 1
        elif instr == 'jmp':
            offset = int(args)
            idx += offset
        elif instr == 'jie':
            reg, offset = args.split(', ')
            offset = int(offset)
            idx += offset if registers[reg] % 2 == 0 else 1
        elif instr == 'jio':
            reg, offset = args.split(', ')
            offset = int(offset)
            idx += offset if registers[reg] == 1 else 1
        else:
            raise ValueError(f'Unknown instruction {instr}')
    return registers

instructions: List[str] = [line.rstrip() for line in sys.stdin]

registers: Dict[str, int] = {'a': 0, 'b': 0}
registers = run(instructions, registers)
print('Part 1:', registers['b'])

registers = {'a': 1, 'b': 0}
registers = run(instructions, registers)
print('Part 2:', registers['b'])
