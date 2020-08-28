with open('input.txt', 'r') as f:
    instructions = [line.rstrip() for line in f.readlines()]

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
x = 1
y = 1
code = ''

for instruction in instructions:
    for letter in instruction:
        if letter == 'U' and y > 0:
            y -= 1
        elif letter == 'R' and x < 2:
            x += 1
        elif letter == 'D' and y < 2:
            y += 1
        elif letter == 'L' and x > 0:
            x -= 1

    code += str(keypad[y][x])

print(code)