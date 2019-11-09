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
            weight = int(m.group(2))
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
            child = get_by_name(child_name, programs)
            count += 1 + get_children_count(child, programs)
    return count

def get_by_name(name, programs):
    return next(p for p in programs if p.name == name)

def part2(root, programs):
    # root = get_by_name('tulwp', programs)
    for child_name in root.children:
        child = get_by_name(child_name, programs)
        print(child.name, get_total_weight(child, programs))

def get_total_weight(p, programs):
    total_weight = p.weight
    if p.children:
        for child_name in p.children:
            child = get_by_name(child_name, programs)
            total_weight += get_total_weight(child, programs)
    return total_weight

if __name__ == '__main__':
    programs = read_input()
    root = part1(read_input())
    print(root.name)
    part2(root, programs)
