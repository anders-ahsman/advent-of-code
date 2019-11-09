import re

class Program:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = children

def read_input():
    with open('input.txt', 'r') as f:
        programs = []

        for line in f.readlines():
            m = re.match(r'(\w+) \((\d+)\)', line)
            name = m.group(1)
            weight = m.group(2)
            program = Program(name, weight)

            separator = '->'
            if separator in line:
                _, children = line.split(separator)
                program.children = [x.strip() for x in children.split(',')]

            programs.append(program)

        return programs

def part1(programs):
    root = next(p for p in programs if is_root(p, programs))
    return root

def is_root(p, programs):
    return get_children_count(p, programs) == len(programs) - 1

def get_children_count(p, programs):
    count = 0
    if p.children:
        for child_name in p.children:
            child = next(c for c in programs if c.name == child_name)
            count += 1 + get_children_count(child, programs)
    return count

if __name__ == '__main__':
    programs = read_input()
    root = part1(programs)
    print(root.name)
