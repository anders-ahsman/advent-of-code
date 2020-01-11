from hashlib import md5

key = 'yzbqklnj'

n = 1
while True:
    md5hash = md5(bytes(key + str(n), 'utf-8')).hexdigest()
    if md5hash[:5] == '00000':
        print('Part 1:', n)
        break
    n += 1

n = 1
while True:
    md5hash = md5(bytes(key + str(n), 'utf-8')).hexdigest()
    if md5hash[:6] == '000000':
        print('Part 2:', n)
        break
    n += 1