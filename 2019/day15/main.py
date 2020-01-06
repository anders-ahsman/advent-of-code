from collections import deque
import curses
import sys

sys.path.append('..')
from common.intcode_computer import IntcodeComputer

tiles = {0: '#', 1: '.', 2: '!'}
directions = {
    1, # north
    2, # south
    3, # west
    4  # east
}
direction_to_pos_change = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
opposite_direction = {1: 2, 2: 1, 3: 4, 4: 3}
turn_left = {1: 3, 2: 4, 3: 2, 4: 1}
turn_right = {1: 4, 2: 3, 3: 1, 4: 2}

def read_input(filename):
    with open(filename, mode='r') as f: # read from file, want to use stdin for keyboard
        program = [int(x) for x in f.readline().split(',')]
    return program

def draw(screen, grid, pos, direction):
    screen.clear()
    for pt in grid:
        screen.addstr(pt[1], pt[0], 'D' if pt == pos else grid[pt])
    screen.addstr(0, 0, f'pos: {pos}, direction: {direction}, len(grid): {len(grid)}')
    screen.refresh()

def part1(screen, program):
    curses.curs_set(False)
    com = IntcodeComputer(program)
    it = com.run()
    start_pos = (25, 25)
    pos = start_pos
    grid = {pos: '.'}
    direction = 1
    while len(grid) < 1659: # todo: stop when repeating path
        grid = get_nbs(pos, grid, com, it)
        wall_on_left_side = grid[get_position(pos, turn_left[direction])] == '#'
        if not wall_on_left_side:
            direction = turn_left[direction]
        pos, res, grid = move(pos, direction, grid, com, it)
        if res == 0: # hit wall
            direction = turn_right[direction]
        draw(screen, grid, pos, direction)
    end_pos = next(k for k, v in grid.items() if v == '!')
    steps_min = bfs(start_pos, end_pos, grid)
    screen.addstr(2, 0, f'min steps from {start_pos} to {end_pos}: {steps_min}')
    screen.getch()

def move(pos, direction, grid, com, it):
    before_move = pos
    com.inputs.append(direction)
    res = next(it)
    assert res in range(3)
    pos = get_position(pos, direction)
    grid[pos] = tiles[res]
    if res == 0: # hit wall
        pos = before_move
    return pos, res, grid

def get_nbs(pos, grid, com, it):
    for direction in range(1, 5):
        before_move = pos
        pos, _, grid = move(pos, direction, grid, com, it)
        if pos != before_move:
            pos, _, grid = move(pos, opposite_direction[direction], grid, com, it)
    return grid

def get_position(pos, direction):
    return tuple([sum(x) for x in zip(pos, direction_to_pos_change[direction])])

def bfs(start, end, grid):
    frontier = deque([start])
    depth = {start: 0}
    while frontier:
        h = frontier.popleft()
        if h == end:
            return depth[h]
        for nb in get_nbs_from_grid(h, grid):
            if nb in depth or grid[nb] == '#':
                continue
            frontier.append(nb)
            depth[nb] = depth[h] + 1

def get_nbs_from_grid(pos, grid):
    x, y = pos
    return [(i, j) for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]]

filename = sys.argv[1]
program = read_input(filename)
curses.wrapper(part1, program)