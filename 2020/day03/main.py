import sys

def read_tree_map():
    return [line.strip() * 100 for line in sys.stdin]


def move(tree_map, delta_x, delta_y):
    pos_x = 0
    pos_y = 0
    count = 0
    try:
        while pos_y < len(tree_map):
            pos_x += delta_x
            pos_y += delta_y
            if tree_map[pos_y][pos_x] == '#':
                count += 1
    except IndexError:
        pass
    return count


if __name__ == '__main__':
    tree_map = read_tree_map()
    print(f'Part 1: {move(tree_map, 3, 1)}')
    print(f'Part 2: {move(tree_map, 1, 1) * move(tree_map, 3, 1) * move(tree_map, 5, 1) * move(tree_map, 7, 1) * move(tree_map, 1, 2)}')
