with open('input.txt', 'r') as f:
    instructions = [(instr[0], int(instr[1:])) for instr in f.readline().split(', ')]

x = 0
y = 0
angle = 0

for turn, distance in instructions:
    if turn == 'L':
        angle = (angle - 90) % 360
    elif turn == 'R':
        angle = (angle + 90) % 360

    if angle == 0:
        y += distance
    elif angle == 90:
        x += distance
    elif angle == 180:
        y -= distance
    elif angle == 270:
        x -= distance

print(abs(x) + abs(y))
