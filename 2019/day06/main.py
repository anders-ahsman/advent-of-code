import sys

def read_input():
    orbits = []
    for line in sys.stdin:
        a, b = line.rstrip().split(')')
        orbits.append((a, b))
    return orbits

def main(orbits):
    planets = set([a for a, b in orbits]).union(set([b for a, b in orbits]))

    planets_to_orbiting = dict()
    for planet in planets:
        orbiting = [b for a, b in orbits if a == planet]
        planets_to_orbiting[planet] = orbiting

    print(calc_total_steps(planets, planets_to_orbiting))

    path_you = calc_path_to_com('YOU', planets_to_orbiting, set())
    path_santa = calc_path_to_com('SAN', planets_to_orbiting, set())
    path_common = set([p for p in path_you]).intersection(set([p for p in path_santa]))
    print(len(path_you.difference(path_common)) + len(path_santa.difference(path_common)))

def calc_total_steps(planets, planets_to_orbiting):
    total_steps = 0
    for p in planets:
        total_steps += calc_steps_for_planet(p, planets_to_orbiting, 0)
    return total_steps

def calc_steps_for_planet(planet, planets_to_orbiting, steps):
    for a, orbiting in planets_to_orbiting.items():
        if planet in orbiting:
            planet = a
            steps += 1 + calc_steps_for_planet(planet, planets_to_orbiting, steps)
            return steps
    return 0

def calc_path_to_com(planet, planets_to_orbiting, path):
    for a, orbiting in planets_to_orbiting.items():
        if planet in orbiting:
            planet = a
            if planet == 'COM':
                return path
            path.add(planet)
            return calc_path_to_com(planet, planets_to_orbiting, path)

if __name__ == '__main__':
    orbits = read_input()
    main(orbits)