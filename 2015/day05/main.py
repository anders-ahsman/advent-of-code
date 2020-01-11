import sys

def read_input():
    strings = []
    for s in sys.stdin:
        strings.append(s)
    return strings

def part1(strings):
    vowels = 'aeiou'
    forbidden_strings = ['ab', 'cd', 'pq', 'xy']
    nice_count = 0
    for string in strings:
        vowel_count = 0
        for vowel in vowels:
            vowel_count += string.count(vowel)
        if vowel_count < 3:
            continue

        repeating_letter = False
        for i in range(1, len(string)):
            ch = string[i]
            last_ch = string[i - 1]
            if ch == last_ch:
                repeating_letter = True
                break
        if not repeating_letter:
            continue

        if any(forbidden in string for forbidden in forbidden_strings):
            continue

        nice_count += 1
    return nice_count

def part2(strings):
    nice_count = 0
    for string in strings:
        repeating_word = False
        for i in range(2, len(string)):
            word = string[i - 2] + string[i - 1]
            if word in string[i:]:
                repeating_word = True
                break

        repeating_letter = False
        for i in range(2, len(string)):
            if string[i - 2] == string[i]:
                repeating_letter = True

        if repeating_word and repeating_letter:
            nice_count += 1
    return nice_count

strings = read_input()
print('Part 1:', part1(strings))
print('Part 2:', part2(strings))