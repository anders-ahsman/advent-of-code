import sys

def read_program():
    return [line.strip() for line in sys.stdin]


def part1(program):
    seen = set()
    acc = 0
    pos = 0
    while True:
        if pos in seen:
            return acc

        seen.add(pos)
        instruction, arg = program[pos].split(' ')
        arg = int(arg)
        if instruction == 'nop':
            pos += 1
        elif instruction == 'acc':
            acc += arg
            pos += 1
        elif instruction == 'jmp':
            pos += arg
        else:
            raise ValueError(f'Unknown instruction: {instruction}')


def part2(program):
    for i in range(len(program)):
        try:
            prog_copy = program[:]
            if 'nop' in prog_copy[i]:
                prog_copy[i] = prog_copy[i].replace('nop', 'jmp')
                return try_program(prog_copy)
            elif 'jmp' in prog_copy[i]:
                prog_copy[i] = prog_copy[i].replace('jmp', 'nop')
                return try_program(prog_copy)
        except StopIteration:
            pass


def try_program(program):
    seen = set()
    acc = 0
    pos = 0
    while pos < len(program):
        if pos in seen:
            raise StopIteration()

        seen.add(pos)
        instruction, arg = program[pos].split(' ')
        arg = int(arg)
        if instruction == 'nop':
            pos += 1
        elif instruction == 'acc':
            acc += arg
            pos += 1
        elif instruction == 'jmp':
            pos += arg
        else:
            raise ValueError(f'Unknown instruction: {instruction}')
    return acc


if __name__ == '__main__':
    program = read_program()
    print(f'Part 1: {part1(program)}')
    print(f'Part 2: {part2(program)}')
