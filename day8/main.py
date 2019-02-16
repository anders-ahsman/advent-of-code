def part1():
    numbers = read_numbers()
    root_node, size = unpack(numbers)
    metadata_sum = get_metadata_sum(root_node)
    print('Metadata sum:', metadata_sum)
    return metadata_sum

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
    children_count = numbers[0]
    metadata_count = numbers[1]

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

if __name__ == '__main__':
    part1()