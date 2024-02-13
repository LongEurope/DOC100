#Hangman project

import random

word_list = []

def choose_word():
    word = random.choice(word_list)

def user_guess():
    global guess
    while True:
        guess = input('Please input a letter\n')
        if len(guess) == 1 and guess.isalpha():
            guess = guess.lower()
            break
        else:
            print('Please input a single letter')

def compare():
    return