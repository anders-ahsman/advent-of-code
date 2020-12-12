import sys


def read_lines():
    return [line.rstrip() for line in sys.stdin]


def create_graph(lines):
    graph = {}
    for line in lines:
        bag_type, contain = line.rstrip().split(' bags contain ')
        if 'no other' in contain:
            contain = []
        else:
            contain = [part for part in contain.split(', ')]
        graph[bag_type] = contain
    return graph


def part1(graph, target, count=0, seen=set()):
    if target in seen:
        return count - 1
    seen.add(target)
    for bag, contain in graph.items():
        if any(target in part for part in contain):
            count = part1(graph, bag, count + 1)
    return count


if __name__ == '__main__':
    lines = read_lines()
    graph = create_graph(lines)
    target = 'shiny gold'
    print(f'Part 1: {part1(graph, target)}')
