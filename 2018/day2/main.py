def part1():
    data = read_input()

    twos = 0
    threes = 0
    for line in data:
        for char in line:
            if line.count(char) == 2:
                twos += 1
                break
        for char in line:
            if line.count(char) == 3:
                threes += 1
                break
    checksum = twos * threes
    return checksum

def read_input():
    with open('input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]
    return data

def part2():
    data = read_input()

    from itertools import combinations
    for line1, line2 in combinations(data, 2):
        different = [x for x, y in zip(line1, line2) if x != y]
        if len(different) == 1:
            common = ''.join([x for x, y in zip(line1, line2) if x == y])
            return common

if __name__ == '__main__':
    checksum = part1()
    print('Checksum:', checksum)

    common_chars = part2()
    print('Common characters:', common_chars)