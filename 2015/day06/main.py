from collections import defaultdict
import re
import sys

def read_input():
    instructions = []
    for s in sys.stdin:
        instructions.append(s)
    return instructions

def part1(instructions):
    grid = defaultdict(bool)
    for instruction in instructions:
        from_x, from_y, to_x, to_y = [int(n) for n in re.findall(r'\d+', instruction)]
        for y in range(from_y, to_y + 1):
            for x in range(from_x, to_x + 1):
                if 'on' in instruction:
                    grid[(x, y)] = True
                elif 'off' in instruction:
                    grid[(x, y)] = False
                else:
                    grid[(x, y)] = not grid[(x, y)]
    return sum(1 for v in grid.values() if v)

def part2(instructions):
    grid = defaultdict(int)
    for instruction in instructions:
        from_x, from_y, to_x, to_y = [int(n) for n in re.findall(r'\d+', instruction)]
        for y in range(from_y, to_y + 1):
            for x in range(from_x, to_x + 1):
                if 'on' in instruction:
                    grid[(x, y)] += 1
                elif 'off' in instruction:
                    grid[(x, y)] -= 1
                    if grid[(x, y)] < 0:
                        grid[(x, y)] = 0
                else:
                    grid[(x, y)] += 2
    return sum(v for v in grid.values())

instructions = read_input()
print('Part 1:', part1(instructions))
print('Part 2:', part2(instructions))
