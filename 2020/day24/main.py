import re
import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def part1(lines):
    tiles = {}
    for line in lines:
        x, y, z = 0, 0, 0
        while len(line) > 0:
            if (m := re.match(r'^nw', line)) is not None:
                line = line[len(m.group(0)):]
                y += 1
                z -= 1
            elif (m := re.match(r'^sw', line)) is not None:
                line = line[len(m.group(0)):]
                x -= 1
                z += 1
            elif (m := re.match(r'^ne', line)) is not None:
                line = line[len(m.group(0)):]
                x += 1
                z -= 1
            elif (m := re.match(r'^se', line)) is not None:
                line = line[len(m.group(0)):]
                y -= 1
                z += 1
            elif (m := re.match(r'^w', line)) is not None:
                line = line[len(m.group(0)):]
                x -= 1
                y += 1
            elif (m := re.match(r'^e', line)) is not None:
                line = line[len(m.group(0)):]
                x += 1
                y -= 1
            else:
                raise ValueError(f'No match for line: {line}')
        tiles[(x, y, z)] = True if (x, y, z) not in tiles else not tiles[(x, y, z)]
    return sum(1 for val in tiles.values() if val)


if __name__ == '__main__':
    lines = read_lines()
    print(f'Part 1: {part1(lines)}')
