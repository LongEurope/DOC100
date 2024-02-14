#Making a caesar cipher machine
#instead of function(1, 2, 3), function(a=1, b=2, c=3 works)
#! Note: to find index of an item in a list, list.index(item)
#! Note: for position in range(len(list)) is very useful
#! Note: if two functions are very similar, you can make a new function that does both of their jobs at once

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, task):
    product = ''
    shift = shift % 26
    if task == 'decode':
        shift *= -1
    for letter in text:
        if letter.isalpha():
            index = alphabet.index(letter)
            new_index = index + shift
            if new_index < 0:
                new_index += 26
            elif new_index > 25:
                new_index -= 26
            new_letter = alphabet[new_index]
            product += new_letter
        else:
            product += letter
    print(f'The {task}d text is {product}')

def get_str(script, valid):
    while True:
        request = input(script)
        if request in valid:
            break
        else:
            print('Please input a valid message.')
    return request

def get_int(script):
    while True:
        request = input(script)
        if request.isdigit():
            request = int(request)
            break
        else:
            print('Please input a valid number')
    return request


#main
print('''
%%%%%%%%%%#+-.     .-+*+.#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%#+.    =#%%%*-    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%*: .  =%%%%%%%%%=  #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%*     =%%%%%%%%%%%+ #%%%%%%##**##%%%%%%%%%##**#%%%%%%%##**#%##%%%%%%%#***#%%%%%%%#####%%%####%%%%
%%%%#.     #%%%%%%%%%%%%%%%%%*  .-    -#%%%%%*.  -   +%%%#=  .:.  -%%%%*...-.   :#%%#+     -*    .#%%%
%%%%*    .:%%%%%%%%%%%%%%%%#.   *%#:   .#%%%:   #%%.   %#=   *%%* :#%%    *%%.    #%%%+      .   :#%%%
%%%%*    .:%%%%%%%%%%%%%%%%#    -%#:   .#%%-   :#%%-   =#:     =%**#%#    =%%:    #%%%+   . *%%##%%%%%
%%%%*     .#%%%%%%%%%%%%%%%%%#*#*.     .#%%.     ..    -%*.      .*%%%%#*#*..   ..#%%%+    :#%%%%%%%%%
%%%%#=     +%%%%%%%%%%%%%%%%%+   =*:   .#%%.    #%%%%%%%%%#+.      +%%%+   +#:    #%%%+    -%%%%%%%%%%
%%%%%#=     *%%%%%%%%%%:*%%# .  +%#:   .#%%-    .#%%%#==#+:%%#-    =%#  . *%%:.   #%%%+    -%%%%%%%%%%
%%%%%%%*.    -#%%%%%*: :#%%#  .  :.     -*##:     .:. -#%= :#%%+   *%*     :.     =+%%+    :#%%%%%%%%%
%%%%%%%%%#+:        :=#%%%%#-    -*+ .  -#%%%*:     :*%%%+.....  -*%%%-    :*#    :##*:    .-*%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%#*=---=*#%%%=#%%%*--*%%%%%%%%%%%%%%%%%%%%#******%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%#+.    :===:     #%%+    =%%%%%%%%%%%%%%%%%%%#+     #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%#+    .*%%%%%%%*   #%%#    *%%%%%%%%%%%%%%%%%%%%#.    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%#-  . :#%%%%%%%%%%. #%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%#=     *%%%%%%%%%%%#=#%=::::-*%*=::::=+-.  .=#%%%%#.  . *=.  :+#%%%%%%*-... =#%%%*-::::+#+:  =#%%%
%%%%*     .%%%%%%%%%%%%%%%%%+    +%%#:     =+:    *%%%#.     ..    -#%%%*   +%#   -%%%+    .      *%%%
%%%%*.    :%%%%%%%%%%%%%%%%%*    +%%%:    *%%%.    #%%#.    #%#:  . *%%#    #%%*   +%%+.    =%#=-#%%%%
%%%%*     .%%%%%%%%%%%%%%%%%*    +%%%:    *%%%=    +%%#.    #%#:.   +%%:   .---:   .%%+    :#%%%%%%%%%
%%%%#:  .  *%%%%%%%%%%%%%%%%*    +%%%:    *%%%=    =%%#.    #%#:    +%%.    #%%%%%%%%%+    :#%%%%%%%%%
%%%%%#.   .:%%%%%%%%%%%%#%%%*    +%%%: .  *%%%-    *%%#.  . #%#:    +%%-    +%%%%%%#%%+    -#%%%%%%%%%
%%%%%%#-    .#%%%%%%%#. *%%%*    +%%%:    +%%%    .%%%#.    #%#:    +%%#.     #%#= *%%+    :#%%%%%%%%%
%%%%%%%%#+      ::..  +#%%%+      *%%:           =#%%#=     -#=     :#%%#-. .    :#%%#:.  . +#%%%%%%%%
%%%%%%%%%%%##*++++**#%%%%%%*******#%%:    *#*++*#%%%%#*******##******#%%%%#*+++*#%%%%#*******#%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:    *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:    *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*-.    :+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      ''')

while True:
    task = get_str(script='Type "encode" to encrypt, and "decode" to decrypt', valid=['encode', 'decode'])
    text = input('Type your message:\n').lower()
    shift = get_int(script='Type the shift number:\n')
    caesar(text=text, shift=shift, task=task)
    keep = get_str(script='Would you like to keep playing? Input "y" to continue, or "n" to stop:\n', valid=['y', 'n'])
    if keep != 'y':
        break