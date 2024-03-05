#learning about dictionaries, nesting lists and dictionaries
#Making a blind auction program
#! Note: look at line 10, making multiple items for a dictionary can be vr useful
#! Note: to clear console, import os, os.system('cls')

import os

#MAIN
participants = {}
winner = {'name': None, 'bid': 0}

os.system('cls')
print('Welcome to blind bidder')
while True:
    os.system('cls')
    name = input('Input the name you wish to be attached for your bid: ')
    bid = int(input('Input the amount of money you wish to bid: '))
    participants[name] = bid
    keep = input('Would you like to add another participant? Enter "y" to add, enter any other key to finish')
    if keep != 'y':
        break
for person in participants:
    if participants[person] > winner['bid']:
        winner['name'] = person
        winner['bid'] = participants[person]

os.system('cls')
print(f'The winner of the auction is {winner["name"]} bidding at ${winner["bid"]}')