import os
import random
import time

#TODO account for blackjack hand

spades = []
diamonds = []
clubs = []
hearts = []
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [spades, diamonds, clubs, hearts]

player= []
dealer = []

def get_answer(prompt, acceptable):
    while True:
        request = str(input(prompt)).lower()
        if request in acceptable:
            break
        else:
            print('Invalid input, please check the acceptable answers.')
    return request

def shuffle():
    for suit in deck:
        for rank in card_ranks:
            suit.append(rank)

def count(hand):
    total = 0
    for card_value in hand:
        if card_value == 'A':
            card_value = 11
        elif card_value == 'K' or card_value == 'Q' or card_value == 'J':
            card_value = 10
        else:
            card_value = int(card_value)
        total += card_value
    if total > 21:
        if 'A' in hand:
            total -= 10
    return total

def deal(hand):
    random_suit = random.choice(deck)
    random_card = random.choice(random_suit)
    random_suit.remove(random_card)
    hand.append(random_card)

def player_round():
    while True:
        action = get_answer(prompt='Would you like to hit or stand? H/S', acceptable=['h', 's'])
        if action == 's':
            break
        elif action == 'h':
            deal(player)
            print(player)
            if count(player) > 21:
                print('Bust')
                break

def dealer_round():
    while count(dealer) < 21:
        deal(dealer)

def round_finish():
    if count(player) > 21:
        if count(dealer) > 21:
            print('Push')
        else:
            print('Lose')
    else:
        if count(dealer) > 21:
            print('Win')
        else:
            if count(player) > count(dealer):
                print('Win')
            elif count(player) < count(dealer):
                print('Lose')
            elif count(player) == count(dealer):
                print('Push')

def shuffle_if_needed():
    card_count = 0
    for suit in deck:
        for card in suit:
            card_count += 1
    if card_count < 39:
        shuffle()

def main():
    os.system('cls')
    keep_playing = 'y'
    while keep_playing == 'y':
        player = []
        dealer = []
        shuffle()
        for _ in range(2):
            deal(player)
            deal(dealer)
        print(f'Dealer\'s hand: {random.choice(dealer)} and hole card')
        print(f'Your hand: {player}')
        player_round()
        dealer_round()
        round_finish()
        shuffle_if_needed()
        keep_playing = get_answer(prompt='Would you like to keep playing? Y/N: ', acceptable=['y', 'n'])
    print('Thank you for playing')

main()