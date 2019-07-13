import random

LETTERS = 'bcdfghjklmnprstvwxzaeiou'
lettersUpper = 'BCDFGHJKLMNPRSTVWXZAEIOU'
SYMBOLS = '!@#$%^&*()?/":;+-§№'
digits  = '1234567890'
letters = list(LETTERS)
lettersUpper = list(lettersUpper)
symbols = list(SYMBOLS)
digits = list(digits)
DEFAULT_PASS_LENGTH = 8
DEFAULT_PASS_NUMBER = 1


def convert_input_to_int(input_data, default_value):
    if not input_data:
        return default_value
    if not input_data.isnumeric():
        print('Input must be numeric', end = "")
        return convert_input_to_int(input("Please retry: "), default_value)
    else:
        return int(input_data)



pass_quant = convert_input_to_int(input("Please enter the quantity of the passwords: "), DEFAULT_PASS_NUMBER)

pass_length = convert_input_to_int(input("And what's the length of the password: "), DEFAULT_PASS_LENGTH)



all_symbols = letters + lettersUpper + symbols + digits

for i in range(pass_quant):
    password = ''
    for j in range(pass_length):
        password += random.choice(all_symbols)
    print(password)
