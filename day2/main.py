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

# Part 2
for idx, line in enumerate(data):
    for line2 in data[idx + 1:]:
        different = [x for x, y in zip(line, line2) if x != y]
        if len(different) == 1:
            common = ''.join([x for x, y in zip(line, line2) if x == y])
            print('Common characters:', common)
            break
