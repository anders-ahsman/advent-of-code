import json
import sys

def get_numbers_sum(data):
    numbers_sum = 0
    if type(data) == dict:
        data = data.values()
    for val in data:
        val_type = type(val)
        if val_type == int:
            numbers_sum += val
        elif val_type in [list, dict]:
            numbers_sum += get_numbers_sum(val)
    return numbers_sum

def get_numbers_sum_ignore_red(data):
    numbers_sum = 0
    is_dict = False
    if type(data) == dict:
        is_dict = True
        data = data.values()
    for val in data:
        val_type = type(val)
        if val_type == int:
            numbers_sum += val
        elif val_type == str:
            if val == 'red' and is_dict:
                return 0
        elif val_type in [list, dict]:
            numbers_sum += get_numbers_sum_ignore_red(val)
    return numbers_sum

input = next(sys.stdin)
data = json.loads(input)
print('Part 1:', get_numbers_sum(data))
print('Part 2:', get_numbers_sum_ignore_red(data))
