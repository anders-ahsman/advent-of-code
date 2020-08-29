from collections import defaultdict
import re

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines

def is_real_room(room: str) -> bool:
    return calculate_checksum(room) == read_checksum(room)

def calculate_checksum(room: str) -> str:
    # Remove sector ID and checksum, e.g. 804[gbiva] from hwbba-gii-fgrctvogpv-804[gbiva]
    letters = room.split('-')
    letters.pop()
    letters_joined = ''.join(letters)

    letter_to_count = defaultdict(int)
    for letter in letters_joined:
        letter_to_count[letter] += 1

    # Sort by letter count first and then by alphabetical order of the letters.
    # Start with rightmost criteria.
    sorted_alphabetically = sorted(letter_to_count)
    checksum = sorted(sorted_alphabetically, key=lambda k: letter_to_count[k], reverse=True)
    return ''.join(checksum[:5])

def read_checksum(room: str) -> str:
    return re.findall(r'\[(\w+)\]', room)[0]

def get_sector_id(room: str) -> int:
    return int(re.findall(r'\d+', room)[0])

if __name__ == '__main__':
    rooms = read_input('input.txt')
    print(sum(get_sector_id(room) for room in rooms if is_real_room(room)))
