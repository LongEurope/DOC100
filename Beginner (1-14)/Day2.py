#Same as day one
#Making a tip calculator. This will be easy af hopefully
#! Note: To print a specific index of a word, do variable[4]
#! Note: To round floats, do round(floatvariable, 2). E.g. in line 45

def get_bill():
    global total
    total = float(input('Please input the total from the bill: $'))

def get_tip():
    global tip_percentage
    while True:
        tip_percentage = input('What percentage tip would you like to give? 10, 12, or 15?: ')
        if tip_percentage == '10':
            tip_percentage = int(tip_percentage)
            tip_percentage = float(tip_percentage/100)
            break
        elif tip_percentage == '12':
            tip_percentage = int(tip_percentage)
            tip_percentage = float(tip_percentage/100)
            break
        elif tip_percentage == '15':
            tip_percentage = int(tip_percentage)
            tip_percentage = float(tip_percentage/100)
            break
        else:
            print('Please input either 10, 12, or 15')
            
def get_people():
    global people
    while True:
        people = input('Please input the amount of people you will share the bill with, if paying by yourself please input 1. ')
        if people.isdigit():
            people = int(people)
            break
        else:
            print('Please input a valid number of people')

def main():
    print('Welcome to the tip calculator')
    get_bill()
    get_tip()
    get_people()
    net_total = total * (1 + tip_percentage)
    each_pay = round(net_total/people, 2)
    print(f'Each person pays ${each_pay}')

main()