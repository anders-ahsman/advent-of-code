import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def read_initial_state(lines):
    state = set()
    z = 0
    for y, line in enumerate(lines):
        for x in range(len(line)):
            state.add((x, y, z))
    return state


def part1(state, cycles=6):
    for _ in range(cycles):
        newstate = state.copy()
        for (x, y, z) in state:
            for dz in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        pos = (x + dx, y + dy, z + dz)
                        neighbour_count = neighbours(state, pos)
                        if (pos in state and 2 <= neighbour_count <= 3) or \
                           (pos not in state and neighbour_count == 3):
                                newstate.add(pos)
        state = newstate
    return len(state)


def neighbours(state, pos):
    count = 0
    x, y, z = pos
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dz == dy == dx == 0:
                    continue
                pos = (x + dx, y + dy, z + dz)
                if pos in state:
                    count += 1
    return count


def read_initial_state2(lines):
    state = set()
    w = 0
    z = 0
    for y, line in enumerate(lines):
        for x in range(len(line)):
            state.add((x, y, z, w))
    return state


def part2(state, cycles=6):
    for _ in range(cycles):
        print(_)
        newstate = state.copy()
        for (x, y, z, w) in state:
            for dw in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            pos = (x + dx, y + dy, z + dz, w + dw)
                            neighbour_count = neighbours2(state, pos)
                            if (pos in state and 2 <= neighbour_count <= 3) or \
                               (pos not in state and neighbour_count == 3):
                                    newstate.add(pos)
        state = newstate
    return len(state)


def neighbours2(state, pos):
    count = 0
    x, y, z, w = pos
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dz == dy == dx == dw == 0:
                        continue
                    pos = (x + dx, y + dy, z + dz, w + dw)
                    if pos in state:
                        count += 1
    return count


if __name__ == '__main__':
    lines = read_lines()
    initial_state = read_initial_state(lines)
    initial_state2 = read_initial_state2(lines)
    print(f'Part 1: {part1(initial_state)}')
    print(f'Part 2: {part2(initial_state2)}')
