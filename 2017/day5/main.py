def read_input():
    with open('input.txt', 'r') as f:
        return [int(offset) for offset in f.readlines()]

def part1(instructions):
    jumps = 0
    pos = 0
    while True:
        offset = instructions[pos]
        instructions[pos] += 1
        pos += offset
        jumps += 1
        if pos < 0 or pos >= len(instructions):
            break
    return jumps

def part2(instructions):
    jumps = 0
    pos = 0
    while True:
        offset = instructions[pos]
        if offset >= 3:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        pos += offset
        jumps += 1
        if pos < 0 or pos >= len(instructions):
            break
    return jumps

if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
