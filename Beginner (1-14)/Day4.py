#Starting to look at day modules and doing interactives, working on random and lists
#! List[x] recalls item at index x in List. negative numbers start going from the end to beginning.
#ChatGPT scary asf it fixed my code in 1 second

# TODO 0 = ROCK | 1 = PAPER | 2 = SCISSORS

import random

keep_playing = True

def get_user():
    global user_choice
    while True:
        user_choice = input('Rock, paper or scissors? Input "0" for rock, "1" for paper, or "2" for scissors: ')
        if user_choice == '0' or user_choice == '1' or user_choice == '2':
            user_choice = int(user_choice)
            break
        else:
            print('Please input a valid number')

def get_com():
    global com_choice
    com_choice = random.randint(0, 2)

def reveal():
    if user_choice == 0:
        print('You chose rock')
    elif user_choice == 1:
        print('You chose paper')
    elif user_choice == 2:
        print('You chose scissors')
    if com_choice == 0:
        print('The computer chose rock')
    elif com_choice == 1:
        print('The computer chose paper')
    elif com_choice == 2:
        print('The computer chose scissors')

def compare():
    if user_choice == 0:
        if com_choice == 0:
            print('Tie')
        elif com_choice == 1:
            print('You lose')
        elif com_choice == 2:
            print('You win')
    elif user_choice == 1:
        if com_choice == 0:
            print('You win')
        elif com_choice == 1:
            print('Tie')
        elif com_choice == 2:
            print('You lose')
    elif user_choice == 0:
        if com_choice == 2:
            print('You lose')
        elif com_choice == 1:
            print('You win')
        elif com_choice == 2:
            print('Tie')

def get_keep():
    global keep_playing
    ask = input('Would you like to keep playing? Input "y" to continue, or any other key to quit.').lower()
    if ask == 'y':
        keep_playing = True
    else:
        keep_playing = False

def main():
    get_user()
    get_com()
    reveal()
    compare()

while keep_playing == True:
    main()
    get_keep()