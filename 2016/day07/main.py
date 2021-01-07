import sys


ips = [l.rstrip() for l in sys.stdin.readlines()]

count_tls = 0
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
    count_tls += is_abba

count_ssl = 0
for ip in ips:
    sequences = ip.replace('[', ']').split(']')
    supernet_seqs = sequences[::2]
    hypernet_seqs = sequences[1::2]

    is_ssl = False
    for sn_seq in supernet_seqs:
        for i in range(len(sn_seq) - 2):
            a, b, c = sn_seq[i], sn_seq[i + 1], sn_seq[i + 2]
            if a != b and a == c:
                bab = f'{b}{a}{b}'
                if any(bab in hn_seq for hn_seq in hypernet_seqs):
                    is_ssl = True
    count_ssl += is_ssl

print(f'Part 1: {count_tls}')
print(f'Part 2: {count_ssl}')
