import re, sys
from collections import defaultdict, namedtuple

def read_input():
    Instruction = namedtuple('Instruction', ['condition', 'action'])
    instructions = []
    for line in sys.stdin:
        m = re.match(r'(.+) if (.+)', line.strip())
        action = m.group(1).replace('inc', '+=').replace('dec', '-=')
        condition = m.group(2)
        instructions.append(Instruction(condition, action))
    return instructions

def exec_instructions(instructions):
    register = defaultdict(int)
    for i in instructions:
        var, rest = i.condition.split(' ', 1)
        condition = str(register[var]) + rest
        if eval(condition):
            var, rest = i.action.split(' ', 1)
            action = 'register[\'' + var + '\'] ' + rest
            exec(action)
    print(max(register.values()))

if __name__ == '__main__':
    instructions = read_input()
    exec_instructions(instructions)