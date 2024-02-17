#Making a calculator app easy asf its k grade btw
#! Note: Right below a function, you can use '''yap yap yap''' for the docstring, e.g. line 28

import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    '''Simple, K grade calculator.'''
    a = float(input('Please input the first number: '))
    sign = input('Please input an operation: ')
    b = float(input('Please input the second number: '))
    ans = operations[sign](a, b)
    print(f'{a} {sign} {b} = {ans}')

    keep = input('Would you like to continue with this answer? Enter "y" to continue, or any other key to start a new calculation\n')

    if keep == 'y':
        while True:
            a = ans
            sign = input('please input an operation: ')
            b = float(input('Please input the next number'))
            ans = operations[sign](a, b)
            print(f'{a} {sign} {b} = {ans}')
            keep = input('Would you like to continue with this answer? Enter "y" to continue, or any other key to start a new calculation\n')
            if keep != 'y':
                break

print('Welcome to K grade calculator')
input('Press enter to continue')
while True:
    os.system('cls')
    calculator()