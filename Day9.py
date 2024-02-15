#learning about dictionaries, nesting lists and dictionaries
#Making a blind auction program
#! Note: to clear console, import os, os.system('cls')

import os

#MAIN
participants = []

def find_highest_bid():
    winning_bidder = {participants[0]}

print('Welcome to blind bidder.')
while True:
    name = input('Please input your name here: ')
    bid = int(input('Please input your bid: '))
    participants.append({name: bid})
    keep = input('Your information has been stored, are there any other participants? Input "y" to add more participants, input any other key to finish the auction.\n')
    if keep != 'y':
        break
    os.system('cls')
os.system('cls')
find_highest_bid()