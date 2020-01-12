from collections import defaultdict
import re
import sys

def read_input():
    instructions = []
    for s in sys.stdin:
        instructions.append(s.rstrip())
    return instructions

def get(x, wires):
    if x == '':
        return None
    if x.isdigit():
        return int(x)
    return wires[x]

def part1and2(instructions):
    wires = defaultdict(lambda: None)
    pattern = r'(\w+)??\s*(\w+)??\s*(\w+)\s->\s(\w+)'
    part_one_answer = None
    while not wires['a']:
        for instruction in instructions:
            a, op, b, dest = re.findall(pattern, instruction)[0]
            a = get(a, wires)
            b = get(b, wires)
            if op == '': # assignment
                if b is not None:
                    wires[dest] = b & 0xffff
            elif op == 'NOT':
                if b is not None:
                    wires[dest] = ~b & 0xffff
            elif op in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
                if a is not None and b is not None:
                    if op == 'AND':
                        wires[dest] = a & b
                    elif op == 'OR':
                        wires[dest] = a | b
                    elif op == 'LSHIFT':
                        wires[dest] = a << b
                    elif op == 'RSHIFT':
                        wires[dest] = a >> b
                    wires[dest] = wires[dest] & 0xffff
            else:
                raise Exception(f'Unknown operator {op}')

            if not part_one_answer and wires['a']:
                part_one_answer = wires['a']
                print('Part 1:', part_one_answer)
                wires = defaultdict(lambda: None)
            if part_one_answer and dest == 'b':
                wires[dest] = part_one_answer

    print('Part 2:', wires['a'])

instructions = read_input()
part1and2(instructions)
