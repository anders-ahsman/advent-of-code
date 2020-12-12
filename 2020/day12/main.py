import sys


def read_instructions():
    return [line.rstrip() for line in sys.stdin]


def part1(instructions):
    x = 0
    y = 0
    angle = 90
    for instruction in instructions:
        action = instruction[:1]
        value = int(instruction[1:])

        if action == 'N':
            y -= value
        elif action == 'S':
            y += value
        elif action == 'W':
            x -= value
        elif action == 'E':
            x += value
        elif action == 'L':
            angle = (angle - value) % 360
        elif action == 'R':
            angle = (angle + value) % 360
        elif action == 'F':
            if angle == 0:
                y -= value
            elif angle == 90:
                x += value
            elif angle == 180:
                y += value
            elif angle == 270:
                x -= value
        else:
            raise ValueError(f'Unknown instruction "{action}"')

    return abs(x) + abs(y)


if __name__ == '__main__':
    instructions = read_instructions()
    print(f'Part 1: {part1(instructions)}')
