import re
import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def part1(lines):
    black_tiles = set()
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
        pos = (x, y, z)
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)
    return black_tiles


def part2(black_tiles):
    for _ in range(100):
        new_black = black_tiles.copy()
        for tile in black_tiles:
            # check black tile and its neighbours
            positions = [(0, 0, 0), (0, 1, -1), (-1, 0, 1), (1, 0, -1), (0, -1, 1), (-1, 1, 0), (1, -1, 0)]
            for (dx, dy, dz) in positions:
                (x, y, z) = tile
                pos = (x + dx, y + dy, z + dz)
                count = black_neighbour_count(pos, black_tiles)
                if pos in black_tiles and (count == 0 or count > 2) and pos in new_black:
                    new_black.remove(pos)
                elif pos not in black_tiles and count == 2:
                    new_black.add(pos)
        black_tiles = new_black
    return black_tiles


def black_neighbour_count(tile, black_tiles):
    count = 0
    neighbours = [(0, 1, -1), (-1, 0, 1), (1, 0, -1), (0, -1, 1), (-1, 1, 0), (1, -1, 0)]
    for (dx, dy, dz) in neighbours:
        (x, y, z) = tile
        pos = (x + dx, y + dy, z + dz)
        if pos in black_tiles:
            count += 1
    return count


if __name__ == '__main__':
    lines = read_lines()
    black_tiles = part1(lines)
    print(f'Part 1: {len(black_tiles)}')
    print(f'Part 2: {len(part2(black_tiles))}')
