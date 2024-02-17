#Taking notes now
#! Note: for number in range(a, b, c): print(number) will print numbers from a to b-1, and c is optional, it stands for increments
#Making a password generator
#! Note: to keep adding to a string, do x += y. This will look like 'xy' in string. E.g. at line 58
#! Note: you can shuffle a list by random.shuffle(list). E.g. at line 56

import random

total_characters = 0
letters_pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_pool = ['!', '@', '#', '$', '%', '&', '*']
numbers_pool = []
password_pool = []
password = ''
for number in range(1, 10):
    numbers_pool.append(number)

def get_letters():
    global letters
    while True:
        letters = input('How many letters will be in your password? ')
        if letters.isdigit():
            letters = int(letters)
            break
        else:
            print('Please input a valid number of letters')

def get_symbols():
    global symbols
    while True:
        symbols = input('How many symbols will be in your password? ')
        if symbols.isdigit():
            symbols = int(symbols)
            break
        else:
            print('Please input a valid number of symbols')

def get_numbers():
    global numbers
    while True:
        numbers = input('How many numbers will be in your password? ')
        if numbers.isdigit():
            numbers = int(numbers)
            break
        else:
            print('Please input a valid number of numbers')

def create():
    global password
    for _ in range(0, letters):
        password_pool.append(random.choice(letters_pool))
    for _ in range(0, symbols):
        password_pool.append(random.choice(symbols_pool))
    for _ in range(0, numbers):
        password_pool.append(random.choice(numbers_pool))
    random.shuffle(password_pool)
    for char in password_pool:
        password += str(char)

def main():
    get_letters()
    get_symbols()
    get_numbers()
    create()
    print(password)

main()