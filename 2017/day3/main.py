from itertools import cycle
from math import floor, sqrt

def part1(target_value):
    directions = cycle([(1, 0), (0, -1), (-1, 0), (0, 1)])
    move_dir = next(directions)

    a = []
    size = floor(sqrt(target_value)) + 3
    for _ in range(size):
        a.append([0] * size)

    start_pos = (floor(size / 2), floor(size / 2))
    pos = start_pos
    value = set_at_pos_and_increase_value(a, pos, 1)

    while value <= target_value:
        # Set current
        pos = add_vecs(pos, move_dir)
        value = set_at_pos_and_increase_value(a, pos, value)

        # Keep moving until able to turn
        check_dir = next(directions)
        check_pos = add_vecs(pos, check_dir)
        while value <= target_value and a[check_pos[1]][check_pos[0]] != 0:
            pos = add_vecs(pos, move_dir)
            value = set_at_pos_and_increase_value(a, pos, value)
            check_pos = add_vecs(pos, check_dir)

        move_dir = check_dir

    steps = abs(pos[0] - start_pos[0]) + abs(pos[1] - start_pos[1])
    return steps

def add_vecs(a, b):
    return tuple([sum(x) for x in zip(a, b)])

def set_at_pos_and_increase_value(a, pos, value):
    a[pos[1]][pos[0]] = value
    return value + 1

if __name__ == '__main__':
    steps = part1(368078)
    print(steps)