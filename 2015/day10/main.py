def look_and_say(seq, times):
    for _ in range(times):
        print(f'{_}/{times}')
        cnt = 1
        next_seq = ''
        while seq:
            ch = seq[0]
            if len(seq) == 1:
                next_seq += str(cnt) + ch
                break

            next_ch = seq[1]
            if ch == next_ch:
                cnt += 1
            else:
                next_seq += str(cnt) + ch
                cnt = 1
            seq = seq[1:]
        seq = next_seq
    return seq

seq = '3113322113'
print('Part 1:', len(look_and_say(seq, 40)))
print('Part 2:', len(look_and_say(seq, 50)))
