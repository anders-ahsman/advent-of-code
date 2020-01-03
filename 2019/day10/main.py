from collections import defaultdict
import math, sys

def read_input():
    astroids = set()
    for y, line in enumerate(sys.stdin):
        for x, col in enumerate(line.rstrip()):
            if col == '#':
                astroids.add((x, y))
    return astroids

def calc_best_position(astroids):
    pos_to_others_asc_distance = defaultdict(list)
    for a1 in astroids:
        pos_to_others_asc_distance[a1] = sorted([a2 for a2 in astroids if a2 != a1],
            key=lambda a: get_distance(a, a1))

    pos_to_visible = defaultdict(list)
    for pos, others in pos_to_others_asc_distance.items():
        seen_angles = set()
        for other in others:
            angle = get_angle(pos, other)
            if angle not in seen_angles:
                pos_to_visible[pos].append(other)
                seen_angles.add(angle)

    max_visible = 0
    max_pos = None
    for pos, visible in pos_to_visible.items():
        if len(visible) > max_visible:
            max_visible = len(visible)
            max_pos = pos

    return max_pos, max_visible

def vaporize_by_laser(astroids, station_pos):
    astroids.remove(station_pos)
    count = 0
    distance_to_station = lambda pos: get_distance(station_pos, pos)
    while astroids:
        angle_to_posistions = defaultdict(list)
        for pos in astroids:
            angle = get_angle(station_pos, pos)
            angle_to_posistions[angle].append(pos)
        for angle in sorted(angle_to_posistions.keys()):
            sorted_by_distance = sorted(angle_to_posistions[angle], key=distance_to_station)
            closest = sorted_by_distance[0]
            astroids.remove(closest)
            count += 1
            if count == 200:
                return closest

def get_angle(a, b):
    dx = b[0] - a[0]
    dy = -(b[1] - a[1])
    angle = math.atan2(dy, dx) * 180 / math.pi
    return (90 - angle) % 360

def get_distance(a, b):
    dx = b[0] - a[0]
    dy = -(b[1] - a[1])
    return math.sqrt(dx ** 2 + dy ** 2)

if __name__ == '__main__':
    astroids = read_input()
    max_pos, max_visible = calc_best_position(astroids)
    print('Part 1:', max_visible)
    n200 = vaporize_by_laser(astroids, max_pos)
    x, y = n200
    print('Part 2:', x * 100 + y)