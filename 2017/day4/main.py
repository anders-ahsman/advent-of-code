def read_input():
    with open('input.txt', 'r') as f:
        return [row.rstrip().split(' ') for row in f.readlines()]

def part1(passphrases):
    valid_count = sum(1 for passphrase in passphrases\
        if not has_duplicate_words(passphrase))
    return valid_count

def has_duplicate_words(passphrase):
    s = set()
    for word in passphrase:
        if word in s:
            return True
        s.add(word)
    return False

def part2(passphrases):
    valid_count = sum(1 for passphrase in passphrases \
        if not has_duplicate_words_as_anagrams(passphrase))
    return valid_count

def has_duplicate_words_as_anagrams(passphrase):
    s = set()
    for word in passphrase:
        if any(w for w in s if are_anagrams(w, word)):
            return True
        s.add(word)
    return False

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    for c1 in s1:
        if sum(1 for c in s1 if c == c1) != sum(1 for c in s2 if c == c1):
            return False
    return True

if __name__ == '__main__':
    passphrases = read_input()
    print(part1(passphrases))
    print(part2(passphrases))