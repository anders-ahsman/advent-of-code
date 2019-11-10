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
    max_value = None
    register = defaultdict(int)
    for i in instructions:
        var, rest = i.condition.split(' ', 1)
        condition = str(register[var]) + rest
        if eval(condition):
            var, rest = i.action.split(' ', 1)
            action = 'register[\'' + var + '\'] ' + rest
            exec(action)
            value = register[var]
            if not max_value or value > max_value:
                max_value = value
    print('final max value', max(register.values()))
    print('highest value ever', max_value)

if __name__ == '__main__':
    instructions = read_input()
    exec_instructions(instructions)