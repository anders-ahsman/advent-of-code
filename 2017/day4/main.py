def read_input():
    with open('input.txt', 'r') as f:
        return [row.rstrip().split(' ') for row in f.readlines()]

def part1(passphrases):
    return sum(1 for passphrase in passphrases if not has_duplicate_words(passphrase))

def has_duplicate_words(passphrase):
    s = set()
    for word in passphrase:
        if word in s:
            return True
        s.add(word)
    return False

if __name__ == '__main__':
    passphrases = read_input()
    print(part1(passphrases))