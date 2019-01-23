def read_coordinates():
    with open('input.txt', 'r') as f:
        coordinates = [[int(num) for num in line.strip().split(', ')]
            for line in f.readlines()]
        return coordinates

def part1():
    coordinates = read_coordinates()
    print(coordinates)

if __name__ == '__main__':
    part1()