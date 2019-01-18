import itertools

with open('input.txt', 'r') as f:
    data = [int(x) for x in f.readlines()]

# Part 1
freq_sum = sum(data)
print('Sum of frequencies:', freq_sum)

# Part 2
seen = {0}
freq = 0
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print('First repeating frequency:', freq)
        break
    seen.add(freq)
