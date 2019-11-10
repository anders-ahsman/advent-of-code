import re, sys
from collections import defaultdict, namedtuple

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

if __name__ == '__main__':
    line = read_input()
    score = get_score(line)
    print(score)