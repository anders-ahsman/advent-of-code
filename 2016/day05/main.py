import hashlib

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

if __name__ == '__main__':
    door_id = 'abbhdwsy'
    print(get_password(door_id))
