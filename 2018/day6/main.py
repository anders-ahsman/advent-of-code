import itertools as it
from collections import Counter

def part1():
    coordinates = read_coordinates()
    closest_coord_map = calc_closest_coord_map(coordinates)
    closest_coord_map = remove_infinite_areas(closest_coord_map)
    max_area = calc_max_area(closest_coord_map)
    print('Part 1 | Largest finite area:', max_area)

def read_coordinates():
    with open('input.txt', 'r') as f:
        return tuple(tuple(int(num) for num in line.strip().split(', '))
            for line in f.readlines())

def calc_closest_coord_map(coordinates):
    max_x = max(coordinates, key=lambda t: t[0])[0] + 1
    max_y = max(coordinates, key=lambda t: t[1])[1] + 1
    closest_coord_map = [[None for x in range(max_x)] for y in range(max_y)]
    for y in range(max_y):
        for x in range(max_x):
            closest_coord_map[y][x] = closest_coordinate((x, y), coordinates)
    return closest_coord_map

def closest_coordinate(point, coordinates):
    coords_with_dists = [(c, manhattan_distance(c, point)) for c in coordinates]
    dists = [manhattan_distance(c, point) for c in coordinates]
    closest_dist = min(dists)
    if dists.count(closest_dist) == 1:
        closest_coord = [c[0] for c in coords_with_dists if c[1] == closest_dist][0]
        return closest_coord
    return None

def manhattan_distance(coord_a, coord_b):
    return abs(coord_a[0] - coord_b[0]) + abs(coord_a[1] - coord_b[1])

def remove_infinite_areas(closest_coord_map):
    near_edge = set()

    max_y = len(closest_coord_map)
    max_x = len(closest_coord_map[0])
    for y in range(max_y):
        for x in range(max_x):
            coord = closest_coord_map[y][x]
            if coord != None and (x == 0 or x == max_x - 1 or y == 0 or y == max_y - 1):
                near_edge.add(coord)

    for coord in near_edge:
        closest_coord_map = remove_instances_of_coord(closest_coord_map, coord)

    return closest_coord_map

def remove_instances_of_coord(coord_map, coord):
    return [[None if c == coord else c for c in row]
        for row in coord_map]

def calc_max_area(closest_coord_map):
    flattened = [c for c in list(it.chain.from_iterable(closest_coord_map)) if c != None]
    most_common_closest_coord = Counter(flattened).most_common()[0]
    occurrences = most_common_closest_coord[1]
    return occurrences

def part2():
    coordinates = read_coordinates()
    max_dist_sum = 10000
    dist_sum_map = calc_distance_sum_map(coordinates, max_dist_sum)
    area = calc_area(dist_sum_map)
    print('Part 2 | Area:', area)

def calc_distance_sum_map(coordinates, max_dist_sum):
    # Manhattan distance from point to coordinate, total sum for all coordinates.
    max_x = max(coordinates, key=lambda t: t[0])[0] + 1
    max_y = max(coordinates, key=lambda t: t[1])[1] + 1
    dist_sum_map = [[None for x in range(max_x)] for y in range(max_y)]
    for y in range(max_y):
        for x in range(max_x):
            dist_sum = sum([manhattan_distance((x, y), c) for c in coordinates])
            if dist_sum < max_dist_sum:
                dist_sum_map[y][x] = dist_sum
            else:
                dist_sum_map[y][x] = None
    return dist_sum_map

def calc_area(dist_sum_map):
    not_none = [dist for dist in list(it.chain.from_iterable(dist_sum_map)) if dist != None]
    area = len(not_none)
    return area

if __name__ == '__main__':
    part1()
    part2()