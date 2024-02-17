#Blackjack dumb dumb version. I already did this easy asf
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]

def deal(hand):
    dealt_card = random.choice(cards)
    hand.append(dealt_card)
    if count(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

def count(hand):
    total_value = 0
    for card_value in hand:
        total_value += card_value
    return total_value

def main():
    dealer = []
    user = []
    user_bust = False
    dealer_bust = False

    for _ in range(2):
        deal(dealer)
        deal(user)

    os.system('cls')

    if count(user) == 21 or count(dealer) == 21:
        print(f'Dealer: {dealer}')
        print(f'User: {user}')
        if count(user) == 21 and not count(dealer) == 21:
            print('You win by blackjack')
        elif count(dealer) == 21 and not count(user) == 21:
            print('You lose by blackjack')
        else:
            print('Tie with blackjacks')
        input('Press enter to continue')
        return

    print(f'The dealer is holding a {dealer[0]}.')
    print(f'Your hand: {user}')
    print(f'Total value is {count(user)}')
    action = input('Enter "h" to hit, "s" to stand')

    while action == 'h' and user_bust != True:
        deal(user)
        os.system('cls')
        print(f'The dealer is holding a {dealer[0]}.')
        print(f'Your hand: {user}')
        print(f'Total value is {count(user)}')
        if count(user) > 21:
            print('Bust')
            user_bust = True
            break
        action = input('Enter "h" to hit, "s" to stand')

    os.system('cls')
    print(f'Dealer\'s hand: {dealer}')
    print(f'Your hand: {user}')

    while count(dealer) < 17:
        deal(dealer)
        os.system('cls')
        print(f'Dealer\'s hand: {dealer}, totalling {count(dealer)}')
        print(f'Your hand: {user}, totalling {count(user)}')
        if count(dealer) > 21:
            dealer_bust = True

    if user_bust:
        if dealer_bust:
            print('Tie')
        else:
            print('You lose')
    else:
        if dealer_bust:
            print('You win')
        else:
            if count(user) < count(dealer):
                print('You lose')
            elif count(user) == count(dealer):
                print('Tie')
            else:
                print('You win')
    input('Press enter to continue')

while True:
    main()
    os.system('cls')
    if input('Would you like to keep playing? Enter "y" to continue, or any other key to exit') != 'y':
        break