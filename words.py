import random

LETTERS = 'bcdfghjklmnprstvwxzaeiou'
LETTERSUPPER = 'BCDFGHJKLMNPRSTVWXZAEIOU'
SYMBOLS = '!@#$%^&*()?/":;+-§№'
DIGITS  = '1234567890'
LETTERS = list(LETTERS)
LETTERSUPPER = list(LETTERSUPPER)
SYMBOLS = list(SYMBOLS)
DIGITS = list(DIGITS)
DEFAULT_PASS_LENGTH = 8
DEFAULT_PASS_NUMBER = 1
all_symbols = LETTERS + LETTERSUPPER + SYMBOLS + DIGITS


def convert_input_to_int(input_data, default_value):
    if not input_data:
        return default_value
    if not input_data.isnumeric():
        print('Input must be numeric', end = "")
        return convert_input_to_int(input("Please retry: "), default_value)
    else:
        return int(input_data)


def pass_generator(quant, length):
    for i in range(quant):
        password = ''
        for j in range(length):
            password += random.choice(all_symbols)
        print(password)

pass_quant = convert_input_to_int(input("Please enter the quantity of the passwords: "), DEFAULT_PASS_NUMBER)

pass_length = convert_input_to_int(input("And what's the length of the password: "), DEFAULT_PASS_LENGTH)

pass_generator(pass_quant, pass_length)
