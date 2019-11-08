def read_input():
    with open('input.txt', 'r') as f:
        return [int(n) for n in f.readline().split()]

def part1_and_2(blocks):
    seen = set()
    steps = 0
    sequences_to_steps = dict()

    while True:
        steps += 1
        target_idx = blocks.index(max(blocks))
        blocks = redistribute(blocks, target_idx)

        sequence = get_representation(blocks)
        if sequence in seen:
            loop_size = steps - sequences_to_steps[sequence]
            return steps, loop_size
        seen.add(sequence)
        sequences_to_steps[sequence] = steps

def redistribute(blocks, idx):
    to_distribute = blocks[idx]
    blocks[idx] = 0
    while to_distribute > 0:
        idx = (idx + 1) % len(blocks)
        blocks[idx] += 1
        to_distribute -= 1
    return blocks

def get_representation(blocks):
    return ''.join([str(x) for x in blocks])

if __name__ == '__main__':
    initial_blocks = read_input()
    steps, loop_size = part1_and_2(initial_blocks)
    print(steps)
    print(loop_size)
