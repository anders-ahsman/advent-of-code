from itertools import cycle

def add_vecs(a, b):
    return tuple([sum(x) for x in zip(a, b)])

def part1(target_value):
    directions = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    move_dir = next(directions)
    value = 2
    pos = (0, 0)
    a = {pos : 1}

    while value <= target_value:
        # Set current
        pos = add_vecs(pos, move_dir)
        a[pos] = value
        value += 1

        # Keep moving until able to turn
        check_dir = next(directions)
        check_pos = add_vecs(pos, check_dir)
        while value < target_value and check_pos in a:
            pos = add_vecs(pos, move_dir)
            a[pos] = value
            value += 1
            check_pos = add_vecs(pos, check_dir)

        move_dir = check_dir

    x, y = pos
    steps = abs(x) + abs(y)
    return steps

if __name__ == '__main__':
    steps = part1(368078)
    print(steps)