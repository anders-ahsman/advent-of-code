import sys

def read_input():
    return next(sys.stdin)

def get_score(line):
    level = 0
    score = 0
    garbage = False
    skip = False
    for c in line:
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif garbage:
            if c == '>':
                garbage = False
        else:
            if c == '<':
                garbage = True
            elif c == '{':
                level += 1
            elif c == '}':
                score += level
                level -= 1
    return score

def get_garbage_count(line):
    count = 0
    garbage = False
    skip = False
    for c in line:
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif garbage:
            if c == '>':
                garbage = False
            else:
                count += 1
        else:
            if c == '<':
                garbage = True
    return count

if __name__ == '__main__':
    line = read_input()
    print('score', get_score(line))
    print('garbage count', get_garbage_count(line))