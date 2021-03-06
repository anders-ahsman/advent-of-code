import sys

def read_input():
    return [list(l.rstrip('\n')) for l in sys.stdin]

def get_neighbours_on(pos, grid):
    rows = len(grid)
    cols = len(grid[0])
    x, y = pos
    neighbours = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
        (x - 1, y), (x + 1, y)
    ]
    on_count = 0
    for x, y in neighbours:
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            continue
        if grid[y][x] == '#':
            on_count += 1
    return on_count

def part1(grid):
    for _ in range(100):
        next_grid = [row[:] for row in grid]
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                neighbours_on = get_neighbours_on((x, y), grid)
                if ch == '#':
                    newch = '#' if 2 <= neighbours_on <= 3 else '.'
                else:
                    newch = '#' if neighbours_on == 3 else '.'
                next_grid[y][x] = newch
        grid = next_grid
    return get_on_count(grid)

def get_on_count(grid):
    on_count = 0
    for row in grid:
        on_count += sum(1 for ch in row if ch == '#')
    return on_count

def part2(grid):
    grid = add_lights_stuck(grid)
    for _ in range(100):
        next_grid = [row[:] for row in grid]
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                neighbours_on = get_neighbours_on((x, y), grid)
                if ch == '#':
                    newch = '#' if 2 <= neighbours_on <= 3 else '.'
                else:
                    newch = '#' if neighbours_on == 3 else '.'
                next_grid[y][x] = newch
        grid = add_lights_stuck(next_grid)
    return get_on_count(grid)

def add_lights_stuck(grid):
    rows = len(grid)
    cols = len(grid[0])
    grid[0][0] = '#'
    grid[0][cols - 1] = '#'
    grid[rows - 1][0] = '#'
    grid[rows - 1][cols - 1] = '#'
    return grid

grid = read_input()
print('Part 1:', part1(grid))
print('Part 2:', part2(grid))
