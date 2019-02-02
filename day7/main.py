import re

def part1():
    requirements = read_requirements()
    order = calc_step_order(requirements)
    print('Part 1:', order)

def read_requirements():
    requirements = []
    with open('input.txt', 'r') as f:
        for row in f.readlines():
            m = re.match(r'Step (\w) must be finished before step (\w) can begin.', row)
            requirements.append((m.group(1), m.group(2)))
    return requirements

def calc_step_order(requirements):
    step_order = ''

    steps = get_unique_steps(requirements)
    while len(steps) > 0:
        steps_only_left_side = []
        for step in steps:
            only_left_side = len([r for r in requirements if r[1] == step]) == 0
            if only_left_side:
                steps_only_left_side.append(step)

        steps_only_left_side.sort()
        step_add = steps_only_left_side[0]

        step_order += step_add
        steps.remove(step_add)
        requirements = [r for r in requirements if r[0] != step_add]

    return step_order

def get_unique_steps(requirements):
    unique = set()
    for s in requirements:
        unique.add(s[0])
        unique.add(s[1])
    return unique

if __name__ == '__main__':
    part1()