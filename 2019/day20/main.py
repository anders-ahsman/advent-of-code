from collections import defaultdict, deque
import sys

def read_input():
    return [l.rstrip() for l in sys.stdin]

def print_maze(maze):
    for row in maze:
        for ch in row:
            print(ch, end='')
        print()

def part1(maze):
    portals, start, end = get_portals(maze)
    print('Part 1:', bfs(maze, start, end, portals))

def get_portals(maze):
    labels_to_portals = defaultdict(list)
    for y, row in enumerate(maze):
        for x, ch in enumerate(row):
            if is_letter(ch):
                for pt in [
                    (x + 1, y),
                    (x, y + 1)
                ]:
                    try:
                        ch2 = maze[pt[1]][pt[0]]
                    except IndexError:
                        continue # outside of map
                    if is_letter(ch2):
                        key = ch + ch2
                        for p in [pt, (x, y)]:
                            nbs = get_neighbours(maze, p, {})
                            if nbs:
                                tile = nbs.pop()
                                break
                        labels_to_portals[key].append(tile)
    portals = {}
    for label, pts in labels_to_portals.items():
        if label == 'AA':
            start = pts[0]
            continue
        if label == 'ZZ':
            end = pts[0]
            continue
        portals[pts[0]] = pts[1]
        portals[pts[1]] = pts[0]
    return portals, start, end

def is_letter(ch):
    return 'A' <= ch <= 'Z'

def bfs(maze, start, target, portals):
    frontier = deque([start])
    distance = {start: 0}
    while frontier:
        h = frontier.popleft()
        if h == target:
            return distance[h]
        for nb in get_neighbours(maze, h, portals):
            if nb in distance:
                continue
            distance[nb] = distance[h] + 1
            frontier.append(nb)

def get_neighbours(maze, node, portals):
    neighbours = set()
    x, y = node
    for pt in [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]:
        try:
            ch = maze[pt[1]][pt[0]]
            if ch == '.':
                neighbours.add(pt)
            if is_letter(ch) and node in portals:
                neighbours.add(portals[node]) # get other end of portal
        except IndexError:
            pass # outside map
    return neighbours

if __name__ == '__main__':
    maze = read_input()
    print_maze(maze)
    part1(maze)