import sys

def read_input():
    wires = []
    for line in sys.stdin:
        wire = [x for x in line.split(',')]
        wires.append(wire)
    return wires

def main(wires):
    pointsets = []
    points_to_step_dicts = []

    for wire in wires:
        pos_x = 0
        pos_y = 0
        steps = 0
        points = set()
        points_to_steps = {}
        for op in wire:
            direction = op[0]
            distance = int(op[1:])
            if direction == 'L':
                for x in range(pos_x - 1, pos_x - distance - 1, -1):
                    steps += 1
                    point = (x, pos_y)
                    points.add(point)
                    if point not in points_to_steps:
                        points_to_steps[point] = steps
                pos_x -= distance
            elif direction == 'R':
                for x in range(pos_x + 1, pos_x + distance + 1):
                    steps += 1
                    point = (x, pos_y)
                    points.add(point)
                    if point not in points_to_steps:
                        points_to_steps[point] = steps
                pos_x += distance
            elif direction == 'D':
                for y in range(pos_y + 1, pos_y + distance + 1):
                    steps += 1
                    point = (pos_x, y)
                    points.add(point)
                    if point not in points_to_steps:
                        points_to_steps[point] = steps
                pos_y += distance
            elif direction == 'U':
                for y in range(pos_y - 1, pos_y - distance - 1, -1):
                    steps += 1
                    point = (pos_x, y)
                    points.add(point)
                    if point not in points_to_steps:
                        points_to_steps[point] = steps
                pos_y -= distance

        pointsets.append(points)
        points_to_step_dicts.append(points_to_steps)

    min_distance = None
    intersections = pointsets[0].intersection(pointsets[1])
    for point in intersections:
        distance = points_to_step_dicts[0][point] + points_to_step_dicts[1][point]
        if not min_distance or distance < min_distance:
            min_distance = distance

    return min_distance

if __name__ == '__main__':
    wires = read_input()
    min_distance = main(wires)
    print('min_distance', min_distance)