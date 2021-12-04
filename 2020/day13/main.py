from itertools import count
import sys


def read_input():
    depature_earliest = int(sys.stdin.readline().rstrip())
    buses = [int(bus) if bus != 'x' else bus for bus in sys.stdin.readline().rstrip().split(',')]
    return depature_earliest, buses


def part1(depature_earliest, buses):
    departure_best_time = sys.maxsize
    departure_best_bus = 0
    for bus in buses:
        if bus == 'x':
            continue
        t = 0
        while t < depature_earliest:
            t += bus
        if t < departure_best_time:
            departure_best_time = t
            departure_best_bus = bus
    return (departure_best_time - depature_earliest) * departure_best_bus


def part2(buses):
    def departs_at(t, bus):
        return t % bus == 0

    t = 0
    step = 1
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        t = next(t2 for t2 in count(t, step) if departs_at(t2 + i, bus))
        step *= bus  # all bus numbers prime!
    return t


if __name__ == '__main__':
    depature_earliest, buses = read_input()
    print(f'Part 1: {part1(depature_earliest, buses)}')
    print(f'Part 2: {part2(buses)}')
