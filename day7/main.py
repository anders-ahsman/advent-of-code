import re

def read_steps():
    steps = []
    with open('input.txt', 'r') as f:
        for row in f.readlines():
            m = re.match(r'Step (\w) must be finished before step (\w) can begin.', row)
            steps.append((m.group(1), m.group(2)))
    return tuple(steps)

def part1():
    steps = read_steps()
    print(steps)

if __name__ == '__main__':
    part1()