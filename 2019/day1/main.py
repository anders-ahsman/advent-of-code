import math
import sys

def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(int(line))
    return lines

def calc_total_fuel_required(masses):
    total_fuel_required = 0
    for mass in masses:
        total_fuel_required += calc_fuel_required(mass)
    return total_fuel_required

def calc_fuel_required(mass):
    partial_sum = 0
    fuel_required = mass
    while True:
        fuel_required = math.trunc(fuel_required / 3) - 2
        if (fuel_required < 0):
            return partial_sum
        partial_sum += fuel_required

if __name__ == '__main__':
    masses = read_input()
    total_fuel_required = calc_total_fuel_required(masses)
    print('total fuel required', total_fuel_required)