import sys

directions = list(next(sys.stdin))

santa_pos = (0, 0)
visted = set([santa_pos])
for direction in directions:
    x, y = santa_pos
    if direction == '<':
        santa_pos = (x - 1, y)
    elif direction == '>':
        santa_pos = (x + 1, y)
    elif direction == 'v':
        santa_pos = (x, y - 1)
    elif direction == '^':
        santa_pos = (x, y + 1)
    visted.add(santa_pos)
print('Part 1:', len(visted))

santa_pos = (0, 0)
robo_pos = (0, 0)
visted = set([santa_pos])
for i, direction in enumerate(directions):
    santa = i % 2 == 0
    x, y = santa_pos if santa else robo_pos

    if direction == '<':
        new_pos = (x - 1, y)
    elif direction == '>':
        new_pos = (x + 1, y)
    elif direction == 'v':
        new_pos = (x, y - 1)
    elif direction == '^':
        new_pos = (x, y + 1)
    visted.add(new_pos)

    if santa:
        santa_pos = new_pos
    else:
        robo_pos = new_pos
print('Part 2:', len(visted))
