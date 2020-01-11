import sys

dimensions = []
for line in sys.stdin:
    l, w, h = [int(n) for n in line.split('x')]
    dimensions.append([l, w, h])

paper_required = 0
for l, w, h in dimensions:
    paper_required += 2*l*w + 2*w*h + 2*h*l
    paper_required += min(l*w, w*h, h*l)
print('Part 1:', paper_required)

ribbon_required = 0
for l, w, h in dimensions:
    ribbon_required += min(2*(l+w), 2*(w+h), 2*(h+l))
    ribbon_required += l*w*h
print('Part 2:', ribbon_required)