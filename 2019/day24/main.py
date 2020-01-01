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

grid = read_input()
part1(grid)
