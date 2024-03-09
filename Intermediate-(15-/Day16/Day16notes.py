#Programming paradigms: Procedural programming, OOP
#Procedural programming executes line by line precisely pretty much
#OOP creates objects with attributes and methods to divide workload
#I got pip
#packages are many modules created put together for a purpose


from prettytable import PrettyTable
from os import system

system('cls')

table = PrettyTable() #OBJECT = CLASS

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"]) #METHOD

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'c' #ATTRIBUTE

print(table)