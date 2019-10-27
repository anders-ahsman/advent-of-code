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

if __name__ == '__main__':
    instructions = read_input()
    print(part1(instructions))
