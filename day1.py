with open('input.txt', 'r') as f:
    input = [int(x) for x in f.readlines()]

# Part 1
freq_sum = sum(input)
print('Sum of frequencies:', freq_sum)

# Part 2
known_freqs = set()
current_freq = 0
stop = False
while stop == False:
    for freq_change in input:
        current_freq += freq_change
        if (current_freq in known_freqs):
            print('First repeating frequency:', current_freq)
            stop = True
            break
        else:
            known_freqs.add(current_freq)
