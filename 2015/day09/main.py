from itertools import permutations
import re
import sys

distances = []
for s in sys.stdin:
    distances.append(s.rstrip())

distance_between = {}
cities = set()
for distance in distances:
    loc_from, loc_to, distance = re.findall(r'(\w+) to (\w+) = (\d+)', distance)[0]
    distance = int(distance)
    distance_between[(loc_from, loc_to)] = distance
    distance_between[(loc_to, loc_from)] = distance
    cities.add(loc_from)
    cities.add(loc_to)

min_distance = None
max_distance = None
for route in permutations(cities):
    route_distance = 0
    for i in range(1, len(route)):
        city_cur = route[i]
        city_last = route[i - 1]
        route_distance += distance_between[(city_cur, city_last)]
    if not min_distance or route_distance < min_distance:
        min_distance = route_distance
    if not max_distance or route_distance > max_distance:
        max_distance = route_distance

print('Part 1:', min_distance)
print('Part 2:', max_distance)
