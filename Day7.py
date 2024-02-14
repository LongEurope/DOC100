#Hangman project
#! 'a'.join(list) joins the items in list together with an 'a' in the middle

import random

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

def get_guess():
    while True:
        function_guess = input('Please input a letter to guess: ')
        if function_guess in guessed:
            print('Already guessed letter.')
        elif len(function_guess) == 1 and function_guess.isalpha():
            function_guess = function_guess.lower()
            break
        else:
            print('Please input a letter')
    return function_guess

def get_keep():
    while True:
        function_keep = input('Please input "y" to keep playing, or any other key to stop playing.\n')
        if len(function_keep) == 1 and function_keep.isalpha():
            function_keep = function_keep.lower()
            break
        else:
            print('Please input a valid key')
    return function_keep


#Main
print('''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
      ''')

while True:
    word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
    lives = 6
    guessed = []
    game_won = False
    game_lost = False
    display = ''
    ever_played = False

    word = random.choice(word_list)
    for _ in word:
        display += '_'
    word_length = len(word)
    while game_won == False and game_lost == False:
        print(hangman_ascii[6 - lives])
        print(display)
        game_guess = get_guess()
        if game_guess not in word:
            lives -= 1
            if lives == 0:
                game_lost = True
                print(hangman_ascii[6])
            print('Letter was not in word')
        else:
            guessed.append(game_guess)
            for index in range(word_length):
                if word[index] == game_guess:
                    display_list = list(display)
                    display_list[index] = game_guess
                    display = ''.join(display_list)
                    if '_' not in display:
                        game_won = True
    if game_lost:
        print(f'The word was {word}')
    elif game_won:
        print(f'You got the word, well done')
    keep = get_keep()
    if keep != 'y':
        break