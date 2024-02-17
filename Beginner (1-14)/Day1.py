#Can't bother with the whole thing, seeing if I can just do the project for the end of the day
#Creating a band name generator, easy af hopefully

#! Note: you can use \n at the end of your string or whatever to skip a line, I used this in this project for the user to input one line below the prompt e.g. line 8

def get_city():
    global city
    city = input('Please enter the city you were born in\n')

def get_petname():
    global pet
    pet = input('Please enter the name of your pet\n')

def combine(city, pet):
    print(f'Your band name could be the {city} {pet}.')

def main():
    print('Welcome to the band name generator.')
    get_city()
    get_petname()
    combine(city, pet)

main()