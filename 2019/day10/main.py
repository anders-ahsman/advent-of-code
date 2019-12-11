from collections import defaultdict
from math import atan2, sqrt
import sys

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

    print(max_pos, max_visible)

def get_angle(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return atan2(dy, dx)

def get_distance(a, b):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

if __name__ == '__main__':
    astroids = read_input()
    calc_best_position(astroids)