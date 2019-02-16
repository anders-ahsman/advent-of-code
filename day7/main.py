import re

def part1():
    requirements = read_requirements()
    order = calc_step_order(requirements)
    print('Part 1:', order)
    return order

def part2():
    requirements = read_requirements()
    worker_count = 5
    time = calc_total_time(requirements, worker_count)
    print('Part 2:', time)
    return time

def read_requirements():
    requirements = []
    with open('input.txt', 'r') as f:
        for row in f.readlines():
            m = re.match(r'Step (\w) must be finished before step (\w) can begin.', row)
            requirements.append((m.group(1), m.group(2)))
    return requirements

def calc_step_order(requirements):
    order = ''

    steps = get_unique_steps(requirements)
    while len(steps) > 0:
        steps_available = get_steps_only_left_side(steps, requirements)
        step_added = steps_available[0]
        order += step_added
        steps.remove(step_added)
        requirements = [r for r in requirements if r[0] != step_added]

    return order

def get_unique_steps(requirements):
    unique_steps = set()
    for r in requirements:
        unique_steps.add(r[0])
        unique_steps.add(r[1])
    return unique_steps

def get_steps_only_left_side(steps, requirements):
    only_left = []
    for step in steps:
        if not [r for r in requirements if r[1] == step]:
            only_left.append(step)
    only_left.sort()
    return only_left

def calc_total_time(requirements, worker_count):
    time = -1
    workers = []
    for _ in range(worker_count):
        workers.append([0, None])

    steps = get_unique_steps(requirements)
    while len(steps) > 0:
        time += 1

        # Has any step completed?
        for idx, worker in enumerate(workers):
            if worker[0] == time and worker[1] != None:
                step_added = worker[1]
                steps.remove(step_added)
                requirements = [r for r in requirements if r[0] != step_added]

        steps_available = get_steps_only_left_side(steps, requirements)
        for step in steps_available:
            step_in_progress = len([w for w in workers if w[1] == step]) > 0
            if step_in_progress:
                continue

            for idx, worker in enumerate(workers):
                worker_available = worker[0] <= time
                if worker_available:
                    worker[0] = time + ord(step) - 4
                    worker[1] = step
                    workers[idx] = worker
                    break

    return time

if __name__ == '__main__':
    part1()
    part2()