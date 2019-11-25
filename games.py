'''
This file holds all the mini games to be implemented in main.py
author = Victoria Poplawski
'''
#       Coin Flip function
import random
import ass
import Main
import sprites


def coinflip():
    '''
    credit to: http://purcellconsult.com/simulate-coin-flipping-in-python/
    :return: random heads or tails
    '''
    sprites.bird()
    coin = ('heads', 'tails')
    flip = random.choice(coin)
    your_choice = input("heads or tails?\n")
    if your_choice == flip:
        ass.text('It landed on {}.\n alright fallow me to the back\n'.format(flip))
        ass.text("Here kid, keep the coin.")
        Main.coin += 1
    else:
        ass.text("Coin landed on {}.\n Dope, fallow me to the printer\n".format(flip))
        ass.text("Here kid, keep the coin.")
        Main.coin += 1
    return flip


def gambling():
    '''
    credit to Dalton for helping figure out custom try statement
    :return: coins and a message
    '''

    class Error(Exception):
        """Base class for other exceptions"""
        pass

    class ValueTooSmallError(Error):
        """Raised when the input value is too small"""
        pass

    class ValueTooLargeError(Error):
        """Raised when the input value is too large"""
        pass

    sprites.catcrouch()
    ass.text("The rules are simple\n")
    ass.text("I roll two dice and if the sum of both are equal to what you guessed then you win two coins\n")
    ass.dell("and if one of the dice lands on your guess then you get one coin\n")
    coi = 0
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    number = 12
    number2 = 2
    num = 0
    while True:
        try:
            ass.text("Pic a number in between 2 and 12")
            i_num = int(input("\n"))
            if i_num > number:
                raise ValueTooLargeError
            elif i_num < number2:
                raise ValueTooSmallError
            num = i_num
            break
        except ValueTooSmallError:
            ass.text("Do you not know how to count? that's too small")
            print()
        except ValueTooLargeError:
            ass.text("Do you not know how to count? that's too big")
            print()
        sumb = rand + rand2
        if i_num == sumb:
            ass.text("Wow! You won two coins")
            Main.coin += 2
        elif rand == i_num or rand2 == i_num:
            ass.text("Cool, new kid, you won one coin")
            Main.coin += 1
        else:
            ass.text("Damn, you're bad at guessing")


def memory():
    '''
    guessing game- in be tween 1 and ten
    :return: coins and a message
    '''
    n = random.randint(1, 10)
    sprites.rat1()
    ass.text("Say a number in between 1 to 10: ")
    guess = input()
    while n != "guess":
        if guess < n:
            ass.text("guess is low")
            ass.text("different number")
            guess = input()
        elif guess > n:
            ass.text("guess is high")
            ass.text("what's an number from 1 to 10: ")
            guess = input()
        else:
            ass.text("Damn, took you long enough!")
            break
        print
