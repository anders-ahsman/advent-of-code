import sys

def read_program():
    return [line for line in sys.stdin]


def part1(program):
    visited = set()
    acc = 0
    pos = 0
    while True:
        if pos in visited:
            return acc

        visited.add(pos)
        instruction, value = program[pos].split(' ')
        value = int(value)
        if instruction == 'nop':
            pos += 1
        elif instruction == 'acc':
            acc += value
            pos += 1
        elif instruction == 'jmp':
            pos = (pos + value) % len(program)
        else:
            raise ValueError(f'Unknown instruction: {instruction}')


if __name__ == '__main__':
    program = read_program()
    print(f'Part 1: {part1(program)}')
