#OOP coffee machine, same requirements as last time

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    request = str(input(f'What would you like? ({menu.get_items()})')).lower()
    if request == 'off':
        break
    elif request == 'report':
        coffee_maker.report()
        money_machine.report()
    elif request in menu.get_items():
        request = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(request):
            if money_machine.make_payment(request.cost):
                coffee_maker.make_coffee(request)
    else:
        print('Please input a valid request.')