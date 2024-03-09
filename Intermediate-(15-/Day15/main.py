#The course wants me to use pycharm but im sticking with vscode
#making coffee machine project

import os

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

MENU = {
    'espresso': {
        'water': 50,
        'milk': 0,
        'coffee': 18,
        'money': 1.5
    },
    'latte': {
        'water': 200,
        'milk': 150,
        'coffee': 24,
        'money': 2.5
    },
    'cappuccino': {
        'water': 250,
        'milk': 100,
        'coffee': 24,
        'money': 3
    }
}

def check_resources(drink):
    if MENU[drink]["water"] > resources['water']:
        print('Sorry, not enough water')
    elif MENU[drink]['milk'] > resources['milk']:
        print('Sorry, there is not enough milk')
    elif MENU[drink]['coffee'] > resources['coffee']:
        print('Sorry, there is not enough coffee')
    else:
        return True

while True:
    os.system('cls')
    request = str(input('What would you like? (espresso/latte/cappuccino)')).lower()
    if request == 'off':
        break
    elif request == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${round(float(resources["money"]), 2)}')
        input('Press enter to exit this screen')
    elif request == 'espresso' or request == 'latte' or request == 'cappuccino':
        coffee = request
        if check_resources(coffee):
            print('Please insert the coins:')
            quarters = int(input('Insert quarters: '))
            dimes = int(input('Insert dimes: '))
            nickels = int(input('Insert nickels: '))
            pennies = int(input('Insert pennies: '))
            total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
            if total < MENU[coffee]['money']:
                print('Sorry, that\'s not enough money. Money refunded.')
                input('Press enter to exit this screen')
            else:
                change = total - MENU[coffee]['money']
                if change != 0:
                    print(f'Thank you, here is the change: ${round(float(change), 2)}')
                else:
                    print('Thank you.')
                resources['water'] -= MENU[coffee]['water']
                resources['milk'] -= MENU[coffee]['milk']
                resources['coffee'] -= MENU[coffee]['coffee']
                resources['money'] += MENU[coffee]['money']
                print(f'Here is your {coffee}. Enjoy!')
                input('Press enter to exit this screen')
        else:
            input('Press enter to exit this screen')
    else:
        print('Please input a valid request.')
        input('Press enter to exit this screen')