def part1(cups):
    cups = [int(x) for x in cups]
    idx = 0
    for _ in range(100):
        # use "double" list to simulate circle
        picked_up = (cups + cups)[idx + 1:idx + 4]

        value = cups[idx]
        dest_value = value - 1
        if dest_value == 0:
            dest_value = max(cups)
        while dest_value in picked_up:
            dest_value -= 1
            if dest_value == 0:
                dest_value = max(cups)
        dest_idx = cups.index(dest_value)

        cups = [c for c in cups[:dest_idx + 1] if c not in picked_up] + \
               picked_up + \
               [c for c in cups[dest_idx + 1:] if c not in picked_up]

        idx = (cups.index(value) + 1) % len(cups)

    return ''.join([str((cups + cups)[i])
                    for i in range(cups.index(1) + 1, cups.index(1) + 9)])


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def part2(cups):
    cups = [int(x) for x in cups] + list(range(10, 1000001))
    nodes = {c : Node(int(c)) for c in cups}
    for c1, c2 in zip(cups, cups[1:] + cups[:1]):
        nodes[c1].next = nodes[c2]

    current = nodes[cups[0]]
    for _ in range(10000000):
        a = current.next
        b = a.next
        c = b.next
        current.next, c.next = c.next, None

        value = current.value
        dest_value = value - 1
        if dest_value == 0:
            dest_value = max(cups)
        while dest_value in (a.value, b.value, c.value):
            dest_value -= 1
            if dest_value == 0:
                dest_value = max(cups)

        dest_node = nodes[dest_value]
        dest_node.next, c.next = a, dest_node.next

        current = nodes[current.value].next

    return nodes[1].next.value * nodes[1].next.next.value


if __name__ == '__main__':
    cups = '326519478'
    print(f'Part 1: {part1(cups)}')
    print(f'Part 2: {part2(cups)}')
