from copy import deepcopy
import sys

def read_input():
    return [list(l.rstrip('\n')) for l in sys.stdin]

def part1(grid):
    seen = set()
    while True:
        key = ''.join([''.join(row) for row in grid])
        if key in seen:
            break
        seen.add(key)

        nextgrid = [row[:] for row in grid]
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                bugs = neighbouring_bugs((x, y), grid)
                if ch == '#':
                    newch = '#' if bugs == 1 else '.'
                else:
                    newch = '#' if 1 <= bugs <= 2 else '.'
                nextgrid[y][x] = newch
        grid = nextgrid

    i = 0
    rating = 0
    for row in grid:
        for ch in row:
            if ch is '#':
                rating += 2 ** i
            i += 1
    print('Part 1:', rating)

def neighbouring_bugs(pt, grid):
    bugs = 0
    for (x, y) in [
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0],     pt[1] - 1),
        (pt[0],     pt[1] + 1)
    ]:
        if not (0 <= x < 5 and 0 <= y < 5):
            continue
        if grid[y][x] == '#':
            bugs += 1
    return bugs

def part2(grid):
    grids = {0: grid}
    emptygrid = []
    for _ in range(5):
        emptygrid.append(['.'] * 5)
    for i in range(1, 105):
        grids[i] = deepcopy(emptygrid)
        grids[i * -1] = deepcopy(emptygrid)

    count = 0
    while count < 200:
        nextgrids = deepcopy(grids)
        for lvl, g in grids.items():
            if lvl in [min(grids), max(grids)]:
                continue # lvl +- 1 can't be used on outer levels
            nextgrid = nextgrids[lvl]
            for y, row in enumerate(g):
                for x, ch in enumerate(row):
                    bugs = neighbouring_bugs_plutoian((x, y), grids, lvl)
                    if ch == '#':
                        newch = '#' if bugs == 1 else '.'
                    else:
                        newch = '#' if 1 <= bugs <= 2 else '.'
                    nextgrid[y][x] = newch
        grids = nextgrids
        count += 1

    print('Part 2:', bug_count(grids))

def bug_count(grids):
    bugs = 0
    for g in grids.values():
        for y, row in enumerate(g):
            for x, ch in enumerate(row):
                if x == 2 and y == 2:
                    continue
                if ch == '#':
                    bugs += 1
    return bugs

def neighbouring_bugs_plutoian(pt, grids, lvl):
    x, y = pt
    check = []

    # same level
    for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not (0 <= x2 < 5 and 0 <= y2 < 5):
            continue
        if x2 == 2 and y2 == 2:
            continue
        check.append((lvl, x2, y2))

    # neighbouring levels
    if x == 0:
        check.append((lvl - 1, 1, 2))
    elif x == 1 and y == 2:
        for y2 in range(5):
            check.append((lvl + 1, 0, y2))
    elif x == 3 and y == 2:
        for y2 in range(5):
            check.append((lvl + 1, 4, y2))
    elif x == 4:
        check.append((lvl - 1, 3, 2))

    if y == 0:
        check.append((lvl - 1, 2, 1))
    elif y == 1 and x == 2:
        for x2 in range(5):
            check.append((lvl + 1, x2, 0))
    elif y == 3 and x == 2:
        for x2 in range(5):
            check.append((lvl + 1, x2, 4))
    elif y == 4:
        check.append((lvl - 1, 2, 3))

    bugs = 0
    for l, x, y in check:
        if grids[l][y][x] == '#':
            bugs += 1
    return bugs

grid = read_input()
part1(grid)
part2(grid)