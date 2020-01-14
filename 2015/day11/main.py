def next_password(pw):
    pw = list(pw)
    while True:
        pw = increase(pw)
        if is_valid(pw):
            return ''.join(pw)

def increase(pw):
    i = len(pw) - 1
    while True:
        next_ord = ord(pw[i]) + 1
        pw[i] = chr(next_ord)
        if next_ord <= ord('z'):
            break
        pw[i] = 'a'
        i -= 1
    return pw

def is_valid(pw):
    for forbidden in ['i', 'o', 'l']:
        if forbidden in pw:
            return False

    increasing_straight = False
    for i in range(len(pw) - 2):
        if ord(pw[i]) == ord(pw[i+1]) - 1 and ord(pw[i]) == ord(pw[i+2]) - 2:
            increasing_straight = True
            break

    pairs_found = set()
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1] and pw[i] not in pairs_found:
            pairs_found.add(pw[i])

    return increasing_straight and len(pairs_found) > 1

part1_answer = next_password('vzbxkghb')
part2_answer = next_password(part1_answer)
print('Part 1: ', part1_answer)
print('Part 2: ', part2_answer)
