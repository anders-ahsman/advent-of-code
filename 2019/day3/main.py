import sys

def read_input():
    wires = []
    for line in sys.stdin:
        wire = [x.replace('\n', '').replace('\r', '') for x in line.split(',')]
        wires.append(wire)
    return wires

def main(wires):
    points_1st_wire = set()
    points_2nd_wire = set()

    for i, wire in enumerate(wires):
        pos_x = 0
        pos_y = 0
        points = set()
        for op in wire:
            direction = op[0]
            distance = int(op[1:])
            if direction == 'L':
                for x in range(pos_x - 1, pos_x - distance - 1, -1):
                    points.add((x, pos_y))
                pos_x -= distance
            elif direction == 'R':
                for x in range(pos_x + 1, pos_x + distance + 1):
                    points.add((x, pos_y))
                pos_x += distance
            elif direction == 'D':
                for y in range(pos_y + 1, pos_y + distance + 1):
                    points.add((pos_x, y))
                pos_y += distance
            elif direction == 'U':
                for y in range(pos_y - 1, pos_y - distance - 1, -1):
                    points.add((pos_x, y))
                pos_y -= distance
        if i == 0:
            points_1st_wire = points
        else:
            points_2nd_wire = points

    intersections = points_1st_wire.intersection(points_2nd_wire)
    return min([abs(x) + abs(y) for x, y in intersections])

if __name__ == '__main__':
    wires = read_input()
    min_distance = main(wires)
    print('min_distance', min_distance)