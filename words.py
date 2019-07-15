import random
import tkinter as tk
import pyperclip
from tkinter import ttk

LETTERS = 'bcdfghjklmnprstvwxzaeiou'
LETTERSUPPER = 'BCDFGHJKLMNPRSTVWXZAEIOU'
SYMBOLS = '!@#$%^&*()?/":;+-§№'
DIGITS = '1234567890'
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
        return 0
        # print('Input must be numeric', end="")
        # return convert_input_to_int(input("Please retry: "), default_value)
    else:
        return int(input_data)


def get_value_from_text_input(text_input, def_value):
    return convert_input_to_int(text_input.get(), def_value)


def pass_generator(text_input_num_of_passwords, text_input_length_of_password, txt_output):
    number_of_pass = get_value_from_text_input(text_input_num_of_passwords, DEFAULT_PASS_NUMBER)
    length_of_pass = get_value_from_text_input(text_input_length_of_password, DEFAULT_PASS_LENGTH)

    for i in range(number_of_pass):
        password = ''
        for j in range(length_of_pass):
            password += random.choice(all_symbols)
        txt_output.insert(1.0, password)


root = tk.Tk()
root.title("Random Password Generator")
root.geometry('350x250')
root.resizable(width=False, height=False)

lbl_num_of_pass = tk.Label(root, text="Please enter the quantity of the passwords: ")
lbl_num_of_pass.grid(column=0, row=0)

lbl_length_of_pass = tk.Label(root, text="And what's the length of the password: ")
lbl_length_of_pass.grid(column=0, row=1)

txt_num_of_passwords = tk.Entry(root, width=5)
txt_num_of_passwords.grid(column=1, row=0)

txt_length_of_password = tk.Entry(root, width=5)
txt_length_of_password.grid(column=1, row=1)

txt_result_output = tk.Text(width=35, height=10, bg="#ffffff", fg='black', wrap=tk.WORD)
txt_result_output.place(x=50, y=50)

btn = tk.Button(root, text="Generate", command=lambda: pass_generator(txt_num_of_passwords, txt_length_of_password, txt_result_output)).place(x=280, y=0)

root.mainloop()
