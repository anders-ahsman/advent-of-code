from collections import defaultdict
import re
import sys

pattern = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
deers = {}
for line in sys.stdin:
    deer, speed, move_interval, rest_interval = re.findall(pattern, line)[0]
    deers[deer] = (int(speed), int(move_interval), int(rest_interval))

position = defaultdict(int)
score = defaultdict(int)
resting = defaultdict(int)
moving = defaultdict(int)
for deer, (_, move_interval, _) in deers.items():
    moving[deer] = move_interval

for time in range(2503):
    for deer, (speed, move_interval, rest_interval) in deers.items():
        if moving[deer]:
            position[deer] += speed
            moving[deer] -= 1
            if not moving[deer]:
                resting[deer] = rest_interval
        elif resting[deer]:
            resting[deer] -= 1
            if not resting[deer]:
                moving[deer] = move_interval

    max_pos = max(position.values())
    for deer, pos in position.items():
        if pos == max_pos:
            score[deer] += 1

print('Part 1:', max(position.values()))
print('Part 2:', max(score.values()))
