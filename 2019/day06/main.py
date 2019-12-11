import sys

def read_input():
    orbits = {}
    for line in sys.stdin:
        a, b = line.rstrip().split(')')
        orbits[b] = a
    return orbits

def main(orbits):
    print(part1(orbits))
    print(part2(orbits))

def part1(orbits):
    orbit_count = 0
    for k, v in orbits.items():
        orbit_count += 1
        while v != 'COM':
            orbit_count += 1
            v = orbits[v]

    return orbit_count

def part2(orbits):
    path_you = get_path_to_com('YOU', orbits)
    path_santa = get_path_to_com('SAN', orbits)
    path_common = path_you.intersection(path_santa)

    return len(path_you.difference(path_common)) + len(path_santa.difference(path_common))

def get_path_to_com(k, orbits):
    path = set()
    v = orbits[k]
    while v != 'COM':
        path.add(v)
        v = orbits[v]

    return path

if __name__ == '__main__':
    orbits = read_input()
    main(orbits)