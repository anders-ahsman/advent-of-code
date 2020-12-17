import sys


def read_initial_state():
    state = {}
    z = 0
    for y, line in enumerate(sys.stdin):
        for x, ch in enumerate(line.rstrip()):
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

if __name__ == '__main__':
    initial_state = read_initial_state()
    print(f'Part 1: {part1(initial_state)}')
