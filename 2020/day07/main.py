import sys

def read_lines():
    graph = {}
    for line in sys.stdin:
        bag_type, contain = line.split('contain')
        bag_type = bag_type.replace(' bags', '').strip()
        contain = contain.strip()
        contain = contain.replace('.','').replace('bags', '').replace('bag', '')
        if 'no other' in contain:
            contain = []
        elif ', ' in contain:
            contain = [part.rstrip() for part in contain.split(', ')]
        else:
            contain = [contain.rstrip()]
        graph[bag_type] = contain
    return graph


def part1(graph, target, count=0, known_targets=set()):
    if target in known_targets:
        return count - 1
    known_targets.add(target)
    for bag, contains in graph.items():
        if any(target in part for part in contains):
            count = part1(graph, bag, count + 1)
    return count


if __name__ == '__main__':
    graph = read_lines()
    target = 'shiny gold'
    print(f'Part 1: {part1(graph, target)}')
