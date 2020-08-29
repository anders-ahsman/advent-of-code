keypad_simple = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']]
keypad_star = [
    [ '',  '', '1',  '',  ''],
    [ '', '2', '3', '4',  ''],
    ['5', '6', '7', '8', '9'],
    [ '', 'A', 'B', 'C',  ''],
    [ '',  '', 'D',  '',  '']]

def read_instructions(filename):
    with open(filename, 'r') as f:
        instructions = [line.rstrip() for line in f.readlines()]
    return instructions

def crack_code(keypad, inst, x, y):
    code = ''
    x_max = len(keypad[0]) - 1
    y_max = len(keypad) - 1
    for instruction in inst:
        for letter in instruction:
            if letter == 'U' and y > 0 and keypad[y - 1][x]:
                y -= 1
            elif letter == 'R' and x < x_max and keypad[y][x + 1]:
                x += 1
            elif letter == 'D' and y < y_max and keypad[y + 1][x]:
                y += 1
            elif letter == 'L' and x > 0 and keypad[y][x - 1]:
                x -= 1
        code += keypad[y][x]
    return code

if __name__ == '__main__':
    instructions = read_instructions('input.txt')
    print(f'Part 1: {crack_code(keypad_simple, instructions, 1, 1)}')
    print(f'Part 2: {crack_code(keypad_star, instructions, 0, 2)}')
