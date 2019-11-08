import re

class Program:
    def __init__(self, name, weight, programs_above=None):
        self.name = name
        self.weight = weight
        self.programs_above = programs_above

def read_input():
    with open('input_short.txt', 'r') as f:
        programs = []

        for line in f.readlines():
            m = re.match(r'(\w+) \((\d+)\)', line)
            name = m.group(1)
            weight = m.group(2)
            program = Program(name, weight)

            separator = '->'
            if separator in line:
                _, programs_above = line.split(separator)
                program.programs_above = [x.strip() for x in programs_above.split(',')]

            programs.append(program)

        return programs

def part1(programs):
    for p in programs:
        print(p.name, p.weight, p.programs_above)

if __name__ == '__main__':
    programs = read_input()
    part1(programs)
