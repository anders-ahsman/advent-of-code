from itertools import combinations
import math
import sys

class Moon:
    def __init__(self, pos_x, pos_y, pos_z):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def __repr__(self):
        return f'pos=<x={self.pos_x:+04}, y={self.pos_y:+04}, z={self.pos_z:+04}>, vel=<x={self.vel_x:+04}, y={self.vel_y:+04}, z={self.vel_z:+04}>'

    def get_energy(self):
        return (abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)) * (abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))

def read_input():
    # todo load from puzzle input
    return [Moon(x, y, z) for x, y, z in
        [(3, -6, 6), (10, 7, -9), (-3, -7, 9), (-8, 0, 4)]] # my input
        # [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]] # ex 1
        # [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)]] # ex 2

def apply_gravity(moons, axes):
    for m1, m2 in combinations(moons, 2):
        for axis in axes:
            pos_axis = f'pos_{axis}'
            vel_axis = f'vel_{axis}'
            m1_pos = getattr(m1, pos_axis)
            m2_pos = getattr(m2, pos_axis)
            m1_vel = getattr(m1, vel_axis)
            m2_vel = getattr(m2, vel_axis)
            if m1_pos < m2_pos:
                setattr(m1, vel_axis, int(m1_vel) + 1)
                setattr(m2, vel_axis, int(m2_vel) - 1)
            elif m1_pos > m2_pos:
                setattr(m1, vel_axis, int(m1_vel) - 1)
                setattr(m2, vel_axis, int(m2_vel) + 1)

def apply_velocity(moons, axes):
    for m in moons:
        for axis in axes:
            pos_axis = f'pos_{axis}'
            vel_axis = f'vel_{axis}'
            pos = int(getattr(m, pos_axis))
            vel = int(getattr(m, vel_axis))
            setattr(m, pos_axis, pos + vel)

def lcm(a, b): # least common multiple
     return abs(a * b) // math.gcd(a, b)

if __name__ == '__main__':
    moons = read_input()
    states_to_time = {}
    t = 0
    while True:
        # if t % 1000000 == 0:
        state = ' # '.join([m.__repr__() for m in moons])
        # print(f't={t} state={state}')
        if state in states_to_time:
            print(f'*** {t} last seen at {states_to_time[state]} | {t - states_to_time[state]}')
            break

        states_to_time[state] = t
        # print(state)
        t += 1

        # axes = ['x', 'y', 'z']
        axes = ['z']
        apply_gravity(moons, axes)
        apply_velocity(moons, axes)

    # for _ in range(1000):
    #     apply_gravity(moons)
    #     apply_velocity(moons)
    # for moon in moons:
    #     print(moon)

    # total_energy = sum([m.get_energy() for m in moons])
    # print(total_energy)