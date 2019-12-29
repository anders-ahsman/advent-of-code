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
    explored = {initial}
    nodes_to_parents = {}
    while frontier:
        node = frontier.popleft()
        value = maze[node]
        if pattern_key.match(value) and value not in keys:
            keys.add(value)
            depth = steps_to_node(node, initial, nodes_to_parents)
            print(f'*** depth: {depth} from {node} ({value}) to {initial} ({maze[initial]})')
            if keys == keys_to_collect:
                print('added last key')
                return depth
            print(f'added key {value}, recursive step')
            return depth + min_steps_to_keys(maze, node, keys_to_collect, keys) # restart from here equipped with new key

        for neighbour in get_neighbours(maze, node, keys):
            if neighbour in explored:
                continue
            frontier.append(neighbour)
            explored.add(neighbour)
            nodes_to_parents[neighbour] = node

    return None # went through everything and never found goal

def steps_to_node(node_from, node_to, nodes_to_parents):
    steps = 0
    parent = nodes_to_parents[node_from]
    while parent != node_to:
        steps += 1
        parent = nodes_to_parents[parent]
    return steps + 1

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