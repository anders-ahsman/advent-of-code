import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def create_graph(lines):
    bag_to_contents = {}
    for line in lines:
        bag, inside = line.rstrip().split(' bags contain ')
        contents = {}
        if 'no other' not in inside:
            for part in inside.split(', '):
                count, color = int(part[0:1]), part[2:]
                contents[color] = count
        bag_to_contents[bag] = contents
    return bag_to_contents


def part1(bag_to_contents, target, count=0, seen=set()):
    if target in seen:
        return count - 1
    seen.add(target)
    for bag in bag_to_contents:
        if any(target in part for part in bag_to_contents[bag]):
            count = part1(bag_to_contents, bag, count + 1)
    return count


if __name__ == '__main__':
    lines = read_lines()
    bag_to_contents = create_graph(lines)
    target = 'shiny gold'
    print(f'Part 1: {part1(bag_to_contents, target)}')
