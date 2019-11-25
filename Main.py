'''
This file holds the main plot and possible story paths of the game
author = Victoria Poplawski
'''

import games
import sprites
import time
import ass

#       Game Statistics
coin = 0

sprites.bunny()
ass.text("Hey, my name is Chris\n")
ass.text("what's your name?")
name = input("\n")
ass.text("Nice to meet you, " + name)
ass.text("\nI'm 13.\n")
time.sleep(1)
ass.text("How old are you?\n")
age = input("\n")

ageCal = int(age) - 13
if int(age) == 13:
    ass.text("Cool! We're the same age")
else:
    ass.text("Oh, then we are " + str(abs(ageCal)) + " years apart")

time.sleep(1)
print()
ass.text("Well now that we're friends I'll show you around your new town\n")
ass.text("and if you'er feeling brave we can go to the scariest place in town?\n")
time.sleep(1)
firstBranch = input("Type 'x' if you feel brave\n")

#        first story branch
#       A1
if firstBranch == "x" or firstBranch == "X":
    ass.text("Awesome! Then we're go to the Sunken House\n")
    time.sleep(1)
    ass.text("Hop on the back of my bike, \nI'll ride us there\n")
    time.sleep(3)
    ass.print_ass()
    sprites.house()
    ass.text("Here we are\n")
    theCoin1 = input("You see a coin on the ground, press x to pick it up.")

    #       second story branch
    #       A1  B1
    if theCoin1 == 'x' or theCoin1 == 'X':
        sprites.bunny()
        ass.text("oh wow...\n ")
        time.sleep(1)
        ass.text("You know those are good luck\n")
        ass.text("And with a little luck we wont get wet from the storm\n")

    #       A1 B2
    else:
        ass.text("Hey! Hurry up!\n")
        ass.text("It's supposed to rain today.\n")
#       A2
else:
    ass.text("Fine, we'll find something boring to do\n")
    time.sleep(1)
    ass.text("Oh! we are going to play with the Tree Gang Kids at the old arcade\n")
    time.sleep(2)
    ass.text("Hop on the back of my bike, \nI'll ride us there\n")
    time.sleep(3)
    ass.print_ass()
    sprites.rat1()
    ass.text("Hey! \nWhats up Chris? \n")
    ass.text("Oh, is this the new kids\n")
    time.sleep(1)
    sprites.bunny()
    ass.text("Yup, they're name is " + name)
    ass.text("\nDo you guys want to join the others gambling for candy,\n")
    time.sleep(.5)
    ass.text("or we can play the memory thing in the back\n")
    time.sleep(1)
    ass.text("I say we toss a coin\n")
    # coin flip
    coins = games.coinflip()
    time.sleep(2)

    #       Second story branch
    #       A2, C1
    if coins == "heads":
        sprites.chicken()
        ass.text("Hello new kid, I'm Terry\n and this is Jerry")
        sprites.catcrouch()
        time.sleep(1)
        games.gambling()
        time.sleep(2)
        print()

    #       A2, C2
    else:
        sprites.rat1()
        ass.text("Ok follow me to the printer room")
        sprites.rat2()
        for x in range(10):
            ass.text("*\n")
            ass.text("The printer doesn't actually work, but we have a different game.\n")
            games.memory()
            ass.text("damn look at that rain\n")
