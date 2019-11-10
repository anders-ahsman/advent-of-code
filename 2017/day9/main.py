import sys

def read_input():
    return next(sys.stdin)

def get_score_and_size(line):
    level = 0
    score = 0
    size = 0
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
                size += 1
        else:
            if c == '<':
                garbage = True
            elif c == '{':
                level += 1
            elif c == '}':
                score += level
                level -= 1
    return score, size

if __name__ == '__main__':
    line = read_input()
    score, size = get_score_and_size(line)
    print('score', score)
    print('size', size)