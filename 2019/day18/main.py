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

def part1(maze):
    for y in range(max(pt[1] for pt in maze) + 1):
        for x in range(max(pt[0] for pt in maze) + 1):
            output = maze[(x, y)] if (x, y) in maze else ' '
            print(output, end='')
        print()

    start = next(pt for pt, ch in maze.items() if ch == '@')
    print('part 1:', min_steps(maze, start, ''))

seen = {}
def min_steps(maze, start, havekeys):
    sortedhavekeys = ''.join(sorted(havekeys))
    if (start, sortedhavekeys) in seen:
        return seen[(start, sortedhavekeys)]

    keys = reachable_keys(maze, start, havekeys)
    if not len(keys):
        answer = 0
    else:
        possibilities = []
        for key, (dist, pt) in keys.items():
            possibilities.append(dist + min_steps(maze, pt, havekeys + key))
        answer = min(possibilities)
    seen[(start, sortedhavekeys)] = answer
    return answer

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
    part1(maze)