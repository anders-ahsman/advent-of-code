from collections import defaultdict, deque
from string import ascii_uppercase
import sys

def read_input():
    return [l.rstrip('\n') for l in sys.stdin]

def print_maze(maze):
    for row in maze:
        for ch in row:
            print(ch, end='')
        print()

def part1(maze):
    portals, start, end = get_portals(maze)
    print('Part 1:', bfs(maze, start, end, portals, use_levels=False))

def part2(maze):
    portals, start, end = get_portals(maze)
    print('Part 2:', bfs(maze, start, end, portals, use_levels=True))

def get_portals(maze):
    labels_to_portals = defaultdict(list)
    for y, row in enumerate(maze):
        for x, ch in enumerate(row):
            if ch not in ascii_uppercase:
                continue
            for pt2 in [(x + 1, y), (x, y + 1)]:
                if pt2[0] > W or pt2[1] > H:
                    continue
                ch2 = maze[pt2[1]][pt2[0]]
                if ch2 not in ascii_uppercase:
                    continue
                label = ch + ch2
                pt = (x, y)
                is_outside = any(p[0] in [0, W] or p[1] in [0, H] for p in [pt, pt2])
                for p in [pt, pt2]:
                    nbs = get_neighbours(maze, p, {}, 0, False)
                    if nbs:
                        tile, _ = nbs.pop()
                        labels_to_portals[label].append((tile, is_outside))
                        continue

    portals = {}
    for label, prts in labels_to_portals.items():
        p1, outside1 = prts[0]
        if label == 'AA':
            start = (p1, 0)
            continue
        if label == 'ZZ':
            end = (p1, 0)
            continue
        p2, outside2 = prts[1]
        portals[p1] = (p2, outside1)
        portals[p2] = (p1, outside2)
    return portals, start, end

def bfs(maze, start, end, portals, use_levels):
    frontier = deque([start])
    distance = {start: 0}
    while frontier:
        h, lvl = frontier.popleft()
        if (h, lvl) == end:
            return distance[(h, lvl)]
        for nb, nblvl in get_neighbours(maze, h, portals, lvl, use_levels):
            if (nb, nblvl) in distance:
                continue
            distance[(nb, nblvl)] = distance[(h, lvl)] + 1
            frontier.append((nb, nblvl))

def get_neighbours(maze, node, portals, lvl, use_levels):
    neighbours = set()
    x, y = node
    for pt in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if pt[0] > W or pt[1] > H:
            continue
        ch = maze[pt[1]][pt[0]]
        if ch == '.':
            neighbours.add((pt, lvl))
        elif ch in ascii_uppercase and node in portals:
            other_side, is_outside = portals[node]
            if use_levels:
                if lvl == 0 and is_outside:
                    continue
                newlvl = lvl - 1 if is_outside else lvl + 1
                neighbours.add((other_side, newlvl))
            else:
                neighbours.add((other_side, 0))
    return neighbours

maze = read_input()
W = len(maze[0]) - 1 # Assumes lines are equally long
H = len(maze) - 1
print_maze(maze)
part1(maze)
part2(maze)