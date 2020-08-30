import hashlib
from typing import List, Optional

def get_password(door_id: str) -> str:
    password = ''
    i = 0
    while True:
        arg = str.encode(f'{door_id}{str(i)}')
        hexdigest = hashlib.md5(arg).hexdigest()
        if hexdigest[:5] == '00000':
            password += hexdigest[5]
            if len(password) == 8:
                break
        i += 1
    return password

def get_better_password(door_id: str) -> str:
    password: List[Optional[str]] = [None, None, None, None, None, None, None, None]
    i = 0
    while True:
        arg = str.encode(f'{door_id}{str(i)}')
        hexdigest = hashlib.md5(arg).hexdigest()
        if hexdigest[:5] == '00000':
            try:
                pos = int(hexdigest[5])
                if pos < 8 and password[pos] == None:
                    password[pos] = hexdigest[6]
                    if None not in password:
                        break
            except ValueError:
                pass
        i += 1
    return ''.join([str(ch) for ch in password])

if __name__ == '__main__':
    door_id = 'abbhdwsy'
    print(f'Part 1: {get_password(door_id)}')
    print(f'Part 2: {get_better_password(door_id)}')
