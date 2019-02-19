import re

def part1():
    stars = read_input()
    fast_forward_to_message(stars)

class Star:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

def read_input():
    with open('input.txt', 'r') as f:
        stars = []
        for row in f.readlines():
            m = re.match(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>', row)
            stars.append(Star(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))
        return stars

def fast_forward_to_message(stars):
    min_area = None
    while True:
        area = calc_area(stars)
        if not min_area or area < min_area:
            min_area = area
            move_stars(stars)
        else:
            # Area is getting bigger, assume minimum was reached last time.
            move_stars_backwards(stars)
            print_stars(stars)
            break

def calc_area(stars):
    min_x, min_y, max_x, max_y = boundaries(stars)
    return (max_x - min_x) * (max_y - min_y)

def boundaries(stars):
    min_x = min_y = max_x = max_y = 0
    for s in stars:
        if s.x < min_x: min_x = s.x
        if s.y < min_y: min_y = s.y
        if s.x > max_x: max_x = s.x
        if s.y > max_y: max_y = s.y
    return min_x, min_y, max_x, max_y

def move_stars(stars):
    for s in stars:
        s.x += s.x_vel
        s.y += s.y_vel

def move_stars_backwards(stars):
    for s in stars:
        s.x -= s.x_vel
        s.y -= s.y_vel

def print_stars(stars):
    min_x, min_y, max_x, max_y = boundaries(stars)
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            row += '#' if is_star_at_pos(stars, x, y) else '.'
        print(row)

def is_star_at_pos(stars, x, y):
    for s in stars:
        if s.x == x and s.y == y:
            return True
    return False

if __name__ == '__main__':
    part1()