from typing import Set, Tuple

def read_instructions(filename):
    with open(filename, 'r') as f:
        instructions = [(instr[0], int(instr[1:])) for instr in f.readline().split(', ')]
    return instructions

def measure_distance(instructions, stop_when_already_visited):
    x = 0
    y = 0
    angle = 0
    visited: Set[Tuple[int, int]] = set()

    for turn, distance in instructions:
        if turn == 'L':
            angle = (angle - 90) % 360
        elif turn == 'R':
            angle = (angle + 90) % 360

        if angle == 0:
            for _ in range(1, distance + 1):
                y += 1
                if stop_when_already_visited and (x, y) in visited:
                    return abs(x) + abs(y)
                visited.add((x, y))
        elif angle == 90:
            for _ in range(1, distance + 1):
                x += 1
                if stop_when_already_visited and (x, y) in visited:
                    return abs(x) + abs(y)
                visited.add((x, y))
        elif angle == 180:
            for _ in range(1, distance + 1):
                y -= 1
                if stop_when_already_visited and (x, y) in visited:
                    return abs(x) + abs(y)
                visited.add((x, y))
        elif angle == 270:
            for _ in range(1, distance + 1):
                x -= 1
                if stop_when_already_visited and (x, y) in visited:
                    return abs(x) + abs(y)
                visited.add((x, y))

    return abs(x) + abs(y)

if __name__ == '__main__':
    instructions = read_instructions('input.txt')
    print(f'Part 1: {measure_distance(instructions, False)}')
    print(f'Part 2: {measure_distance(instructions, True)}')
