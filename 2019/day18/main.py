import sys

def read_input():
    maze = {}
    for y, line in enumerate(sys.stdin):
        for x, char in enumerate(line.rstrip()):
            if char != '#':
                maze[(x, y)] = char
    return maze

def part1(maze):
    pos = None
    for y in range(30):
        for x in range(100):
            if (x, y) in maze:
                output = maze[(x, y)]
                if output == '@':
                    output = '.'
                    pos = (x, y)
            else:
                output = ' '
            print(output, end='')
        print()
    print(pos)

if __name__ == '__main__':
    maze = read_input()
    part1(maze)