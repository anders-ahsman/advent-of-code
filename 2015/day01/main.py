import sys

directions = next(sys.stdin)
up_count = directions.count('(')
down_count = directions.count(')')
floor = up_count - down_count
print('Part 1:', floor)

current_floor = 0
for i, direction in enumerate(directions):
    up = direction == '('
    current_floor += 1 if up else -1
    if current_floor == -1:
        print('Part 2:', i + 1)
        break
