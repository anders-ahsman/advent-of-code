import sys


def read_public_keys():
    card_public, door_public = [int(line) for line in sys.stdin]
    return card_public, door_public


def part1(card_public, door_public):
    def get_loop_size(key):
        value = 1
        loop_size = 0
        while True:
            value *= 7
            value = value % 20201227
            loop_size += 1
            if value == key:
                return loop_size
    card_loop_size = get_loop_size(card_public)
    door_loop_size = get_loop_size(door_public)

    def transform(subject_number, loop_size):
        value = 1
        for _ in range(loop_size):
            value *= subject_number
            value = value % 20201227
        return value

    a = transform(door_public, card_loop_size)
    b = transform(card_public, door_loop_size)
    assert a == b
    return a


if __name__ == '__main__':
    card_public, door_public = read_public_keys()
    print(f'Part 1: {part1(card_public, door_public)}')
