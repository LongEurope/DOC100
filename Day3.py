#Day three, similar thing
#! variable % integer == remainder. Can be used to check divisibility
#Choose your own adventure game for project. This is easy asf hopefully
#! You can put .lower at the end of an input or whatever to lowercase everything. E.g. at line 115

end_game = False
farting = False

def gap():
    print('-------------------------------------------------------------------------------------------------------')

def bad_road():
    global end_game
    end_game = True
    gap()
    print('It\'s best not to take risks when you\'re unsure of the consequences. You continue on the highway.')
    print('As you keep going, a large log blocks the entire highway, you come to a stop, wondering how a log could block a highway.')
    print('As soon as you come to a stop, you hear the light but frantic footsteps of those around you approaching your car.')
    print('You try to reverse, but something blocks the way. You look to the right outside your window.')
    print('A man in what seems like a costume of a priest but in all black and wearing the skull of a goat holding a hammer smashes your car window and reaches in.')
    print('You reopen your eyes after the shattering of the window stops ringing in your ears, and when you reopen them')
    print('you see that the man wearing the skull of the goat in front of you without the separation of your car door. He has opened the car door through the broken window.')

def good_road():
    gap()
    print('You need to get off this highway, who knows where you\'ll end up if you keep going.')
    print('After a few twists you reach what looks like a relatively small town. You pass a pub, it had a small parking lot but it had no cars.')
    print('You decide to keep driving around the town until you see some place to stay, or somewhere to rest at least. Since you already passed the pub, you just keep driving until there\'s another turn.')
    print('But after only a short distance, theres a large gate blocking the entire road. You come to a stop in front of the gate.')
    print('You\'re starting to get a really bad feeling. You feel like you must not stay in this car. The hair on your arms stand, and a chill runs down your spine.')

def bad_gate():
    global end_game
    end_game = True
    gap()
    print('You ignore your gut. Getting out of your car in the middle of the night is how a character always dies in a cliche horror story.')
    print('You try to do a three point turn, since the road is a little tight. But as you turn start moving the stick from D to R, you feel something clink on the bottom of you car')
    print('You try to reverse, but the car only revs. You start to realise your car is starting to rise. The last time you had an edible was yesterday, surely the effect has wore off?')
    print('You open the car door, and look outside. You see nothing. You look towards the back of the car, and see that a silhouette of a man has raised your car with a car jack.')
    print('You also realise that for the car to rise, a total of four men would have surrounded your car now. And you car is useless. You slam the car door shut again and panic.')
    print('You decide to make a run for it. You open the car door and prepare to bolt as hard as you can directly outside.')
    print('But as soon as you open the door, a man in what seems like a costume of a priest in all black, but wearing the skull of a goat blocks your way.')

def good_gate():
    gap()
    print('The safety of your car starts to feel like a trap rather than a reassurance. You decide to get out, but as you walk out, something catches your eye.')
    print('You see a man towards the back of your car raising your car with a car jack.')
    print('But for your whole car to be raised from its wheels, there must be four men raising your car this moment. You run before you tell your body to.')
    print('You realise you\'re running the way you took to the gate. Whatever, you can\'t change directions now anyway.')
    print('Just under the sound of your frantic breath and the desperate slamming of your shoes on the damp concrete, you can hear the same of many behind you.')
    print('You keep running, and eventually you see the bar that you\'ve passed on the way here. You\'re going to run past the entry at this rate.')

def enter():
    global end_game
    end_game = True
    gap()
    print('You decide to enter the pub, there\'s no guarantee you can outrun what sounds like 4 or 5 men. And you cant bear to be alone anymore.')
    print('You barge into the pub, but you halt your entire momentum the moment you enter, for there are 4 men in what seems like a costume of a priest in black, but wearing goat skulls on their heads.')
    print('They stare you with the empty black voids the eye sockets of the goat skulls they have on their heads. Their arms are unsettlingly by their sides.')

def keep_running():
    global end_game
    end_game = True
    gap()
    print('This whole town seems off, you feel a sense that something is waiting for you to enter the pub, and you decide to keep running.')
    print('You\'ve never ran so hard before, but the running is effortless for you, as if your innate human drive to survive has taken over.')
    print('But this drive is cut short by you running into something in the darkness and falling back on your ass, but at least the running behind you has stopped now, you\'re safe.')
    print('You stand up, and swipe the dust off your pants, and look back forward. You realise the thing you ran into wasn\'t a tree, or a pole.')
    print('It was a man in a costume that resembled a priest, but in black. The man was also wearing the skull of a goat on his head.')

def fart():
    global end_game
    end_game = True
    global farting
    farting = True
    gap()
    print('⠀⠠⠐⢤⠀⡠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣝⢺⠀⠀⠀                ')
    print('⠉⠄⠃⡌⢃⠲⣄⣣⢩⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡬⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠁⢀⠃⠜⣠⢛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⡈⠐⠤⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣃⠼⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣦⠱⣜⡰⢤⡉⢖⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⢶⢾⣶⣲⡶⣐⣢⢠⡀⠀⢀⠀⠃⢜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠼⠻⣄⠣⣄⠻⢄⢣⠘⡇⠀⠀⠀⠀⠀⣠⣤⣿⣟⡻⡟⡜⠛⢧⣟⠿⣟⣜⢟⣤⠀⠃⡟⣘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣿⣷⣶⣶⠀⠐⠈⡀⠁⠁⠀⠀⠀⣠⣾⣿⣿⣿⣾⡻⡱⠘⣠⡶⣜⡻⣼⣹⢞⡵⢗⡀⡇⢬⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣤⣦⣴⡎⠰⠶⣶⣦⣤⠠⠀⠀⣰⣿⣿⣿⣟⣷⡛⠣⢍⣶⣷⣿⣿⣽⣷⣿⣯⡿⣎⢯⢻⢠⡇⠀⠀⠀⢀⣠⣴⠄⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠈⠐⠓⠈⠀⠀⢱⣿⡷⠈⠀⠠⣿⣿⣿⣯⣻⠸⣡⢻⣧⣾⣽⣿⣿⣿⣿⣿⣿⡷⣩⣏⣯⢧⡇⠀⠀⣾⣿⣿⣿⡂⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⡠⣄⠤⣬⠀⣄⣀⣁⣀⠀⡆⢰⠛⠛⠛⠷⠯⠝⠤⠚⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⢥⣿⣞⢧⢧⠀⠀⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣵⣿⣥⠈⠀⡭⢁⠺⠾⡅⡇⠀⠀⠀⠀⠀⠀⢀⣠⡴⠐⠀⠀⠈⠉⠙⠛⠛⣿⡿⣚⡿⣏⢾⢟⣆⠀⣿⣿⣿⢿⡅⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠿⠿⠿⣿⠇⡇⣠⠿⢧⡄⠃⠰⣄⣀⡀⠀⠠⠟⢋⣴⣴⣶⠆⠀⠀⠀⠀⠠⠸⡟⣽⣷⡽⢾⣟⢹⡆⢻⣿⣿⣟⡆⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣿⣿⣿⢿⡇⠻⠛⠁⡀⡇⢸⠀⠸⣉⣉⡣⡀⠀⠈⠃⠉⠅⠀⠀⠀⠀⠀⠀⠡⣏⣿⣿⣯⣿⢹⣾⢯⣻⣿⣿⢯⡇⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣿⣷⠺⢿⣧⠰⠀⠀⠀⣷⢸⠀⠘⢿⠙⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⣿⣞⡿⡧⢇⡖⣿⢫⢳⣝⡩⣩⣷⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣛⣋⣟⣻⣟⠠⡁⠀⠀⣿⠀⠀⠀⠈⠏⠁⠀⠀⢀⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⣾⣳⣏⣷⣿⣯⢟⢩⠞⣫⣷⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣀⣿⣿⣿⣿⡆⠁⠀⠀⣿⠀⡇⠀⠀⠈⡀⠱⢆⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣿⡿⣾⣏⢿⣏⣿⣾⢾⣹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠻⢿⣿⣿⣿⡆⡃⠀⠠⣿⡄⡇⠀⠀⠀⠱⡀⢤⣠⢤⡞⡟⠃⠀⠀⠀⢀⡴⣾⠟⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣟⣾⣛⣻⣻⣇⢁⠀⠀⠙⡇⢡⠀⠀⠀⠀⣸⣦⡰⣠⠥⠀⠀⠀⠀⣐⣾⡾⠃⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣿⣿⣟⣻⣯⣭⢠⠀⠀⠀⠁⢸⠀⢀⡠⣾⣿⣿⣿⣦⣀⣀⣠⣰⣿⠟⠁⠀⠀⠀⠀⣠⣯⣿⣿⣿⣙⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣿⣿⣿⠿⠿⠿⢦⠀⠀⠀⠀⢸⢸⣿⣵⣿⣿⡿⣿⣿⣿⢻⡟⠋⠁⠀⠀⠀⣀⡴⡞⠣⠚⢰⣿⣯⣍⣸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⣿⣯⣽⣽⣿⣿⡐⠀⠀⠀⠀⠈⠛⢹⣾⣿⣿⣿⣾⣿⣡⣿⠀⠀⠀⠀⣠⠞⡺⢘⣨⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀')
    print('⡿⣽⢾⣟⡛⠻⠅⢢⣀⡀⠀⠀⡄⣿⣿⣿⣿⡿⠻⠉⠁⠌⢖⣤⣔⣯⣷⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀')
    print('⢟⣙⡂⢁⠉⠉⠀⠀⢱⣴⣶⡆⠇⣿⣿⣿⠏⡀⡄⠃⠃⠂⠑⢎⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀')
    print('⣿⣿⣷⢹⣿⢻⡁⠀⠘⣿⣿⡇⢳⣿⣿⣿⠀⢅⠀⠀⣋⠉⠳⠠⣙⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀')
    print('⣿⣿⣿⠿⢾⠳⡟⢊⠽⣻⠿⣷⣿⣿⣿⣿⣧⣤⡠⠀⠁⠐⢄⣅⣿⣿⡟⣧⣿⣿⣫⣿⢯⣿⣿⣯⣿⣿⣟⡷⣿⣿⣿⣿⣟⣿⡿⣿⣿⡄')
    print('⠋⠚⡅⡏⡌⠓⣬⠈⡆⠉⣾⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⠛⣾⣵⢻⣿⣿⣽⣿⣿⢳⣿⣯⣿⣯⡟⣿⣿⣿⡟⣿⣯⣿⣿⣿⡄')
    print('⢎⠧⡱⢌⠱⢢⢅⠊⡔⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣯⡾⣿⡵⣟⡽⣾⣿⣟⡟⣾⣿⣿⡿⣾⣽⣿⣿⣿⣿⣿⢿⣯⣷⣿⡇')
    print('⡎⡖⡱⢊⠥⣃⠎⠒⣼⣿⣿⣿⣯⣻⣟⡿⣿⣿⣿⣾⣿⣿⣿⣿⣯⣾⣷⣾⣿⢿⣟⡷⣏⢳⣿⣻⣿⣟⡷⣯⢿⣿⣟⣿⣿⣿⣻⣽⣿⠀')
    print('⡑⣄⢣⢡⡒⡤⢎⠑⣿⣿⣿⣿⣮⠽⣾⣿⣿⣿⣻⢿⣿⣿⣿⣿⣿⡿⣟⣯⣟⡿⣾⡝⢎⣽⣟⣿⣿⣾⣿⣿⣛⣳⣿⣻⢷⡿⣿⣿⣿⠀')
    print('⠱⡈⢆⠡⡘⢄⠢⢌⣿⣿⣿⣤⡬⠥⢶⡬⣽⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⢿⡾⣟⣧⣻⢮⣿⣿⣿⣟⣯⢷⣯⢿⣟⣿⣿⣿⣿⣿⣻⣿⡀')
    print('⡑⢌⠢⠑⠌⠂⠃⠁⠘⣿⣭⢧⣿⣿⣿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣯⣻⣙⠞⡴⣿⣿⣿⣿⣻⢾⣭⣟⡾⣻⣾⣿⣿⣿⣿⣿⣿⣽⣷')
    print('Good Job')

def main():
    print('You are driving through the night, it\'s been a while since you were on this rundown highway, and you start to get nervous that you\'re lost.')
    while True:
        if end_game == True:
            break
        road = input('As your anxiety rises, a fork in the road appears. You can either merge to the left lane to exit the highway, or continue. Will you "exit", or will you "continue"? ').lower()
        if road == 'exit':
            good_road()
            while True:
                if end_game == True:
                    break
                gate = input('You can either stay in the safety of your car, or you could get out. Will you "stay", or "get out"? ').lower()
                if gate == 'get out':
                    good_gate()
                    bar = input('You need to make the decision now, there are lights on in the bar, maybe people are in there. Will you "enter", or keep "running"? ').lower()
                    if bar == 'enter':
                        enter()
                        break
                    elif bar == 'keep running':
                        keep_running()
                        break
                    elif bar == 'think you the shit bitch you not even the fart':
                        fart()
                        break
                    else:
                        print('Please input "enter", or "keep running" to progress')
                elif gate == 'stay':
                    bad_gate()
                    break
                else:
                    print('Please input "stay", or "get out" to progress.')
        elif road == 'continue':
            bad_road()
            break
        else:
            print('Please input "exit", or "continue" in order to progress.')
    if farting == False:
        print('Who knows what they\'ll do to you, may God have mercy on you.')
        print('Game Over.')
    else:
        print('Munch')

main()