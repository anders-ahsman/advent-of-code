import sys


def read_input():
    depature_earliest = int(sys.stdin.readline().rstrip())
    buses = [int(time_bus) for time_bus in sys.stdin.readline().rstrip().split(',') if time_bus != 'x']
    return depature_earliest, buses


def part1(depature_earliest, buses):
    departure_best_time = sys.maxsize
    departure_best_bus = 0
    for time_bus in buses:
        time = 0
        while time < depature_earliest:
            time += time_bus
        if time < departure_best_time:
            departure_best_time = time
            departure_best_bus = time_bus
    return (departure_best_time - depature_earliest) * departure_best_bus


if __name__ == '__main__':
    depature_earliest, buses = read_input()
    print(f'Part 1: {part1(depature_earliest, buses)}')
