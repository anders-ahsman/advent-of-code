def part1():
    numbers = read_numbers()
    root_node, size = unpack(numbers)
    metadata_sum = get_metadata_sum(root_node)
    print('Part 1:', metadata_sum)
    return metadata_sum

def part2():
    numbers = read_numbers()
    root_node, size = unpack(numbers)
    node_value = get_node_value(root_node)
    print('Part 2:', node_value)
    return node_value

def read_numbers():
    with open('input.txt', 'r') as f:
        row = f.readline()
        numbers = [int(x) for x in row.split(' ')]
    return numbers

class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

def unpack(numbers):
    children_count, metadata_count = numbers[:2]
    children = []
    idx = 2
    for i in range(children_count):
        child, child_size = unpack(numbers[idx:])
        children.append(child)
        idx += child_size

    metadata = numbers[idx:idx + metadata_count]
    node = Node(children, metadata)
    size = idx + metadata_count
    return node, size

def get_metadata_sum(node):
    metadata_sum = sum(node.metadata)
    for c in node.children:
        metadata_sum += get_metadata_sum(c)
    return metadata_sum

def get_node_value(node):
    if not node.children:
        return sum(node.metadata)

    value = 0
    for idx in node.metadata:
        try:
            child = node.children[idx - 1]
            value += get_node_value(child)
        except IndexError:
            pass

    return value

if __name__ == '__main__':
    part1()
    part2()