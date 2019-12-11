def calc_number_of_passwords(range_lower, range_upper):
    return sum(1 for password in range(range_lower, range_upper + 1)
        if is_valid(password))

def is_valid(password):
    password = str(password)
    digits = [int(n) for n in password]
    prev_digit = None
    any_adjacent_digits_same = False
    for i, digit in enumerate(digits):
        if i == 0:
            prev_digit = digit
        else:
            prev_digit = digits[i - 1]
            if digit < prev_digit:
                return False
            elif digit == prev_digit:
                any_adjacent_digits_same = True

    if not any_adjacent_digits_same:
        return False

    exactly_twice = False
    for n in range(1, 11):
        if not exactly_twice and password.count(str(n)) == 2:
            exactly_twice = True

    return exactly_twice

if __name__ == '__main__':
    number_of_passwords = calc_number_of_passwords(271973, 785961)
    print('number_of_passwords', number_of_passwords)