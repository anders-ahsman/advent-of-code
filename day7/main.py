import re

def part1():
    requirements = read_requirements()
    order = determine_order(requirements)
    print('Part 1:', order)

def read_requirements():
    requirements = []
    with open('input.txt', 'r') as f:
        for row in f.readlines():
            m = re.match(r'Step (\w) must be finished before step (\w) can begin.', row)
            requirements.append((m.group(1), m.group(2)))
    return requirements

def determine_order(requirements):
    order = ''

    unique_steps = get_unique_steps(requirements)
    while len(unique_steps) > 0:
        steps_only_in_first = []
        for step in unique_steps:
            only_in_first = len([r for r in requirements if r[1] == step]) == 0
            if only_in_first:
                steps_only_in_first.append(step)

        steps_only_in_first.sort()
        step_to_add = steps_only_in_first[0]

        requirements = [r for r in requirements if r[0] != step_to_add]
        unique_steps = [s for s in unique_steps if s != step_to_add]

        order += step_to_add

    return order

def get_unique_steps(requirements):
    unique = set()
    for s in requirements:
        unique.add(s[0])
        unique.add(s[1])
    return unique

if __name__ == '__main__':
    part1()