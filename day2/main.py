import itertools

with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

# Part 1
twos = 0
threes = 0
for line in data:
    for char in line:
        if line.count(char) == 2:
            twos += 1
            break
    for char in line:
        if line.count(char) == 3:
            threes += 1
            break
checksum = twos * threes
print('Checksum:', checksum)
