from collections import deque
import re, sys

pattern_accessible = re.compile('[.@a-z]')
pattern_door = re.compile('[A-Z]')
pattern_key = re.compile('[a-z]')

def read_input():
    maze = {}
    for y, line in enumerate(sys.stdin):
        for x, char in enumerate(line.rstrip()):
            maze[(x, y)] = char
    return maze

def print_maze(maze):
    for y in range(max(pt[1] for pt in maze) + 1):
        for x in range(max(pt[0] for pt in maze) + 1):
            output = maze[(x, y)] if (x, y) in maze else ' '
            print(output, end='')
        print()

def part1_and_2(maze):
    starts = tuple(pt for pt, ch in maze.items() if ch == '@')
    print('Min steps:', min_steps(maze, starts, ''))

seen = {}
def min_steps(maze, starts, havekeys):
    sortedhavekeys = ''.join(sorted(havekeys))
    if (starts, sortedhavekeys) in seen:
        return seen[(starts, sortedhavekeys)]

    keys = reachable4(maze, starts, havekeys)
    if not len(keys):
        steps = 0
    else:
        possibilities = []
        for ch, (dist, pt, roi) in keys.items():
            nstarts = tuple(pt if i == roi else s for i, s in enumerate(starts))
            possibilities.append(dist + min_steps(maze, nstarts, havekeys + ch))
        steps = min(possibilities)
    seen[(starts, sortedhavekeys)] = steps
    return steps

def reachable4(maze, starts, havekeys):
    keys = {}
    for i, start in enumerate(starts):
        for ch, (dist, pt) in reachable_keys(maze, start, havekeys).items():
            keys[ch] = dist, pt, i
    return keys

def reachable_keys(maze, start, havekeys):
    frontier = deque([start])
    distance = {start: 0}
    keys = {}
    while frontier:
        pt = frontier.popleft()
        ch = maze[pt]
        if pattern_key.match(ch) and ch not in havekeys:
            keys[ch] = distance[pt], pt
            continue # do not explore neighbours of found key
        for neighbour in get_neighbours(maze, pt, havekeys):
            if neighbour in distance:
                continue
            frontier.append(neighbour)
            distance[neighbour] = distance[pt] + 1
    return keys

def get_neighbours(maze, node, havekeys):
    neighbours = set()
    x, y = node
    for pt in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        ch = maze[pt]
        if pattern_accessible.match(ch) or (pattern_door.match(ch) and ch.lower() in havekeys):
            neighbours.add(pt)
    return neighbours

if __name__ == '__main__':
    maze = read_input()
    print_maze(maze)
    part1_and_2(maze)