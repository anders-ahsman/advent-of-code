import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def read_initial_state(lines):
    state = {}
    z = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            state[(x, y, z)] = ch
    return state


def part1(state):
    for _ in range(6):
        newstate = dict(state)
        for pos in state:
            x, y, z = pos
            for dz in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        newpos = (x + dx, y + dy, z + dz)
                        if newpos in state and state[newpos] == '#':
                            newstate[newpos] = '#' if 2 <= neighbours(state, newpos) <= 3 else '.'
                        elif newpos in state and state[newpos] == '.' or newpos not in state:
                            newstate[newpos] = '#' if neighbours(state, newpos) == 3 else '.'
        state = newstate
    return list(state.values()).count('#')


def neighbours(state, pos):
    count = 0
    x, y, z = pos
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dz == dy == dx == 0:
                    continue
                npos = (x + dx, y + dy, z + dz)
                if npos in state and state[npos] == '#':
                    count += 1
    return count


def read_initial_state2(lines):
    state = {}
    w = 0
    z = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            state[(x, y, z, w)] = ch
    return state


def part2(state):
    for _ in range(6):
        newstate = dict(state)
        for pos in state:
            x, y, z, w = pos
            for dw in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            newpos = (x + dx, y + dy, z + dz, w + dw)
                            if newpos in state and state[newpos] == '#':
                                newstate[newpos] = '#' if 2 <= neighbours2(state, newpos) <= 3 else '.'
                            elif newpos in state and state[newpos] == '.' or newpos not in state:
                                newstate[newpos] = '#' if neighbours2(state, newpos) == 3 else '.'
        state = newstate
    return list(state.values()).count('#')


def neighbours2(state, pos):
    count = 0
    x, y, z, w = pos
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dz == dy == dx == dw == 0:
                        continue
                    npos = (x + dx, y + dy, z + dz, w + dw)
                    if npos in state and state[npos] == '#':
                        count += 1
    return count


if __name__ == '__main__':
    lines = read_lines()
    initial_state = read_initial_state(lines)
    initial_state2 = read_initial_state2(lines)
    print(f'Part 1: {part1(initial_state)}')
    print(f'Part 2: {part2(initial_state2)}')
