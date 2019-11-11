#       Victoria Poplawski
#       Text based advanture game


import games
import sprites
import time
import ass

#       Game Statistics
coins = 0

sprites.bunny()
ass.dell("Hey, my name is Chris\n")
ass.dell("what's your name?")
name = input("\n")
ass.dell("Nice to meet you, " + name)
ass.dell("\nI'm 13.\n")
time.sleep(1)
ass.dell("How old are you?\n")
age = input("\n")

ageCal = int(age) - 13
if int(age) == 13:
    ass.dell("Cool! We're the same age")
else:
    ass.dell("Oh, then we are " + str(abs(ageCal)) + " years apart")

time.sleep(1)
print()
ass.dell("Well now that we're friends I'll show you around your new town\n")
ass.dell("and if you'er feeling brave we can go to the scariest place in town?\n")
time.sleep(1)
firstBranch = input("Type 'x' if you feel brave\n")

#        first story branch
#       A1
if firstBranch == "x" or firstBranch == "X":
    ass.dell("Awesome! Then we're go to the Sunken House\n")
    time.sleep(1)
    ass.dell("Hop on the back of my bike, \nI'll ride us there\n")
    time.sleep(3)
    ass.ass2()
    sprites.house()
    ass.dell("Here we are\n")
    theCoin1 = input("You see a coin on the ground, press x to pick it up.")

#       second story branch
#       A1  B1
    if theCoin1 == 'x' or theCoin1 == 'X':
        sprites.bunny()
        ass.dell("oh wow...\n ")
        time.sleep(1)
        ass.dell("You know those are good luck\n")
        ass.dell("And with a little luck we wont get wet from the storm\n")

#       A1 B2
    else:
        ass.dell("Hey! Hurry up!\n")
        ass.dell("It's supposed to rain today.\n")
#       A2
else:
    ass.dell("Fine, we'll find something boring to do\n")
    time.sleep(1)
    ass.dell("Oh! we are going to play with the Tree Gang Kids at the old arcade\n")
    time.sleep(2)
    ass.dell("Hop on the back of my bike, \nI'll ride us there\n")
    time.sleep(3)
    ass.ass2()
    sprites.rat1()
    ass.dell("Hey! \nWhats up Chris? \n")
    ass.dell("Oh, is this the new kids\n")
    time.sleep(1)
    sprites.bunny()
    ass.dell("Yup, they're name is " + name)
    ass.dell("\nDo you guys want to join the others gambling for cards,\n")
    time.sleep(.5)
    ass.dell("or we can play the printer game\n")
    time.sleep(1)
    ass.dell("I say we toss a coin\n")
    coin = games.coinflip()
    time.sleep(2)


#       Second story branch
#       A2, C1
    if coin == "heads":
        sprites.chicken()
        ass.dell("Hello new kid, I'm Terry\n and this is Jerry")
        sprites.catcrouch()
        time.sleep(1)
        games.gambling()
        time.sleep(2)
        ass.dell()


#       A2, C2
    else:
        sprites.rat1()
        ass.dell("Ok follow me to the printer room")
        sprites.rat2()
        for x in range(10):
            ass.dell("*\n")
            ass.dell("The printer doesn't actually work, but we have a different game.\n")
            games.memory()
            ass.dell("damn look at that rain\n")
