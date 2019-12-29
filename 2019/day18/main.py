from collections import deque
import re, sys

pattern_accessible = re.compile('[.@a-z]')
pattern_door = re.compile('[A-Z]')
pattern_key = re.compile('[a-z]')

def read_input():
    maze = {}
    for y, line in enumerate(sys.stdin):
        for x, char in enumerate(line.rstrip()):
            if char != '#':
                maze[(x, y)] = char
    return maze

def part1(maze):
    for y in range(max(pos[1] for pos in maze) + 1):
        for x in range(max(pos[0] for pos in maze) + 1):
            output = maze[(x, y)] if (x, y) in maze else ' '
            print(output, end='')
        print()

    initial = next(pos for pos, value in maze.items() if value == '@')
    keys_to_collect = {value for key, value in maze.items() if pattern_key.match(value)}
    steps = min_steps_to_keys(maze, initial, keys_to_collect)
    print(f'steps: {steps}')

def min_steps_to_keys(maze, initial, keys_to_collect, keys=set()):
    frontier = deque([initial])
    distance = {initial: 0}
    while frontier:
        node = frontier.popleft()
        value = maze[node]
        if pattern_key.match(value) and value not in keys:
            keys.add(value)
            depth = distance[node] - distance[initial]
            print(f'*** depth: {depth} from {node} ({value}) to {initial} ({maze[initial]})')
            if keys == keys_to_collect:
                print('added last key')
                return depth
            print(f'added key {value}, recursive step')
            return depth + min_steps_to_keys(maze, node, keys_to_collect, keys) # restart from here equipped with new key

        for neighbour in get_neighbours(maze, node, keys):
            if neighbour in distance:
                continue
            frontier.append(neighbour)
            distance[neighbour] = distance[node] + 1

    return None # went through everything and never found goal

def get_neighbours(maze, node, keys):
    x, y = node
    neighbours = set()
    for pos, value in maze.items():
        if pos not in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            continue
        if pattern_accessible.match(value) or (pattern_door.match(value) and value.lower() in keys):
            neighbours.add(pos)
    return neighbours

if __name__ == '__main__':
    maze = read_input()
    part1(maze)