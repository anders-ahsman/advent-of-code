from itertools import cycle
from math import floor, sqrt

def spiral_memory(target_value, calc_value, calc_final_value):
    directions = cycle([(1, 0), (0, -1), (-1, 0), (0, 1)])
    move_dir = next(directions)

    a = []
    size = floor(sqrt(target_value)) + 3
    for _ in range(size):
        a.append([0] * size)

    start_pos = (floor(size / 2), floor(size / 2))
    pos = start_pos
    value = calc_value(a, pos)

    while value <= target_value:
        # Set current
        pos = add_vecs(pos, move_dir)
        value = calc_value(a, pos)

        # Keep moving until able to turn
        check_dir = next(directions)
        check_pos = add_vecs(pos, check_dir)
        while value <= target_value and a[check_pos[1]][check_pos[0]] != 0:
            pos = add_vecs(pos, move_dir)
            value = calc_value(a, pos)
            check_pos = add_vecs(pos, check_dir)

        move_dir = check_dir

    return calc_final_value(value, a, pos, start_pos)

def add_vecs(a, b):
    return tuple([sum(x) for x in zip(a, b)])

def part1_set_value():
    count = 1

    def inner(a, pos):
        nonlocal count
        a[pos[1]][pos[0]] = count
        count += 1
        return count

    return inner

def part1_final_value(value, a, pos, start_pos):
    return abs(pos[0] - start_pos[0]) + abs(pos[1] - start_pos[1])

def part2_set_value():
    value = None

    def inner(a, pos):
        x = pos[0]
        y = pos[1]

        nonlocal value
        if not value:
            value = 1
        else:
            value = \
                sum(a[y - 1][x - 1 : x + 2]) + \
                sum(a[y    ][x - 1 : x + 2]) + \
                sum(a[y + 1][x - 1 : x + 2])
        a[y][x] = value
        return value

    return inner

def part2_final_value(value, a, pos, start_pos):
    return value

if __name__ == '__main__':
    puzzle_input = 368078
    print(spiral_memory(puzzle_input, part1_set_value(), part1_final_value))
    print(spiral_memory(puzzle_input, part2_set_value(), part2_final_value))