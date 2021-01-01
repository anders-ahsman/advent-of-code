import re
import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def create_graph(lines):
    bag_to_contents = {}
    for line in lines:
        contents = {}
        m = re.match(r'^(\w+ \w+) bags contain (.*)', line)
        bag, inside = m[1], m[2]
        if 'no other' not in inside:
            for part in inside.split(', '):
                m = re.match(r'(\d) (\w+ \w+) bag', part)
                count, color = int(m[1]), m[2]
                contents[color] = count
        bag_to_contents[bag] = contents
    return bag_to_contents


def part1(bag_to_contents, target_bag):
    holds_target_bag = set()
    def check(target_bag):
        for bag in bag_to_contents:
            if target_bag in bag_to_contents[bag]:
                holds_target_bag.add(bag)
                check(bag)

    check(target_bag)
    return len(holds_target_bag)


def part2(bag_to_contents, target_bag):
    contents = bag_to_contents[target_bag]
    if len(contents) == 0:
        return 0

    return sum(count * (1 + part2(bag_to_contents, bag)) \
               for bag, count in contents.items())


if __name__ == '__main__':
    lines = read_lines()
    bag_to_contents = create_graph(lines)
    target_bag = 'shiny gold'
    print(f'Part 1: {part1(bag_to_contents, target_bag)}')
    print(f'Part 2: {part2(bag_to_contents, target_bag)}')
