def read_input():
    with open('input.txt', 'r') as f:
        return [row.rstrip().split(' ') for row in f.readlines()]

def part1(passphrases):
    return sum(1 for passphrase in passphrases if is_valid(passphrase))

def is_valid(passphrase):
    s = set()
    for word in passphrase:
        if word in s:
            return False
        s.add(word)
    return True

if __name__ == '__main__':
    passphrases = read_input()
    print(part1(passphrases))