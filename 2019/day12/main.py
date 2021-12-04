from itertools import combinations
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
        return f'pos=<x={self.pos_x}, y={self.pos_y}, z={self.pos_z}>, vel=<x={self.vel_x}, y={self.vel_y}, z={self.vel_z}>'

    def get_energy(self):
        return (abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)) * (abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))

def read_input():
    # todo
    moons = []
    for x, y, z in [(3, -6, 6), (10, 7, -9), (-3, -7, 9), (-8, 0, 4)]:
    # for x, y, z in [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]:
        moons.append(Moon(x, y, z))
    return moons

def apply_gravity(moons):
    for m1, m2 in combinations(moons, 2):
        for axis in ['x', 'y', 'z']:
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

def apply_velocity(moons):
    for m in moons:
        for axis in ['x', 'y', 'z']:
            pos_axis = f'pos_{axis}'
            vel_axis = f'vel_{axis}'
            pos = int(getattr(m, pos_axis))
            vel = int(getattr(m, vel_axis))
            setattr(m, pos_axis, pos + vel)

if __name__ == '__main__':
    moons = read_input()
    for _ in range(1000):
        apply_gravity(moons)
        apply_velocity(moons)
    for moon in moons:
        print(moon)

    total_energy = sum([m.get_energy() for m in moons])
    print(total_energy)