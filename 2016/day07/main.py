import sys


ips = [l.rstrip() for l in sys.stdin.readlines()]

count = 0
for ip in ips:
    is_hypernet = False
    is_abba = False
    for i in range(len(ip) - 3):
        a, b, c, d = ip[i], ip[i + 1], ip[i + 2], ip[i + 3]
        if a == '[':
            is_hypernet = True
        elif a == ']':
            is_hypernet = False
        elif a == d and b == c and a != b:
            if is_hypernet:
                is_abba = False
                break
            else:
                is_abba = True
    count += is_abba

print(f'Part 1: {count}')
