#This is so fucked up

import os

os.makedirs(r'.\Path learning\Letters', exist_ok=True)

with open(r'DOC100\Intermediate-(15-\Day24\Path learning\names.txt', mode='r') as invited_names:
    premature_names = invited_names.readlines() #Each line of the text (i.e. name) gets appended into a list
    names = []
    for grossname in premature_names:
        names.append(grossname.strip()) #remove \n

    for name in names:
        with open(fr'.\Path learning\Letters\{name}_letter.txt', mode='w') as letter:
            letter.write(f"Dear {name}, you are invited to the Iron Fist Tournament.\nHope you are there.\n\nBandai Namco.\n")