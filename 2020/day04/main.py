import re
import sys

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def read_passports():
    passports = []
    lines = [line.strip() for line in sys.stdin]
    passport = {}
    for line in lines:
        if line == '':
            passports.append(passport)
            passport = {}
            continue
        items = line.split(' ')
        for item in items:
            k, v = item.split(':')
            passport[k] = v
    passports.append(passport)
    return passports


def check_valid(passports):
    valid_count = 0
    for passport in passports:
        if all(field in passport for field in required_fields):
            valid_count += 1
    return valid_count


def check_valid2(passports):
    valid_count = 0
    for passport in passports:
        valid = True
        for field in required_fields:
            if field not in passport:
                valid = False
            elif field == 'byr' and not (1920 <= int(passport['byr']) <= 2020):
                valid = False
            elif field == 'iyr' and not (2010 <= int(passport['iyr']) <= 2020):
                valid = False
            elif field == 'eyr' and not (2020 <= int(passport['eyr']) <= 2030):
                valid = False
            elif field == 'hgt':
                if 'cm' not in passport['hgt'] and 'in' not in passport['hgt']:
                    valid = False
                if 'cm' in passport['hgt'] and not (150 <= int(passport['hgt'].replace('cm', '')) <= 193):
                    valid = False
                elif 'in' in passport['hgt'] and not (59 <= int(passport['hgt'].replace('in', '')) <= 76):
                    valid = False
            elif field == 'hcl':
                pattern = r'^#[0-9a-fA-F]{6}$'
                m = re.match(pattern, passport['hcl'])
                if not m:
                    valid = False
            elif field == 'ecl':
                valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if not any(color in passport['ecl'] for color in valid_colors):
                    valid = False
            elif field == 'pid':
                pattern = r'^\d{9}$'
                m = re.match(pattern, passport['pid'])
                if not m:
                    valid = False
        if valid:
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    passports = read_passports()
    print(f'Part 1: {check_valid(passports)}')
    print(f'Part 2: {check_valid2(passports)}')
