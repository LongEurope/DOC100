#Hangman project
#! 'a'.join(list) joins the items in list together with an 'a' in the middle

import random

word_list = ['aardvark', 'beaver', 'cat']
lives = 6
guessed = []
game_won = False
game_lost = False
display = ''
ever_played = False

hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def keep():
    global keep
    while True:
        keep = input('Would you like to keep playing? Enter "y" to continue, or any other key to stop: \n')
        if keep.isalpha():
            break
        else:
            print('Please input a valid number.')

def choose_word():
    global word
    global display
    global word_length
    word = random.choice(word_list)
    for _ in word:
        display += '_'
    word_length = len(word)

def life_lost():
    global game_lost
    if lives == 0:
        game_lost = True
    print(hangman_ascii[6 - lives])
    print(f'You have {lives} left.')


def user_guess():
    global game_won
    global guess
    global lives
    global display
    while True:
        guess = input('Please input a letter\n')
        if guess in guessed:
            print('You have already chosen that letter.')
        elif len(guess) == 1 and guess.isalpha():
            guess = str(guess)
            guessed.append(guess)
            if guess not in word:
                lives = lives - 1
                life_lost()
            elif guess in word:
                for index in range(word_length):
                    if word[index] == guess:
                        display_list = list(display)
                        for index in range(word_length):
                            if word[index] == guess:
                                display_list[index] = guess
                                display = ''.join(display_list)
                    if '_' not in display:
                        game_won = True
            break
        else:
            print('Please input a letter')

def main():
    global ever_played
    global lives
    global guessed
    global display
    while True:
        if ever_played == True:
            if game_lost:
                print(f'The word was {word}')
            elif game_won:
                print('Well done')
            keep()
            if keep != 'y':
                break
        ever_played = True
        lives = 6
        guessed = []
        game_won = False
        game_lost = False
        display = ''
        choose_word()
        while game_won == False and game_lost == False:
            print(display)
            user_guess()

main()