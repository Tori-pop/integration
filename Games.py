

#       Coin Flip function
import random
import ass


def coinflip():
    coin = ('heads', 'tails')
    flip = random.choice(coin)
    your_choice = input("heads or tails?\n")
    if your_choice == flip:
        ass.dell('It landed on {}.\n alright fallow me to the back\n'.format(flip))
    else:
        ass.dell("Coin landed on {}.\n Dope, fallow me to the printer\n".format(flip))
    return flip


def gambling():
    class Error(Exception):
        """Base class for other exceptions"""
        pass

    class ValueTooSmallError(Error):
        """Raised when the input value is too small"""
        pass

    class ValueTooLargeError(Error):
        """Raised when the input value is too large"""
        pass

    ass.dell("The rules are simple\n")
    ass.dell("I roll two dice and if the sum of both are equal to what you guessed then you win two coins\n")
    ass.dell("and if one of the dice lands on your guess then you get one coin\n")
    coi = 0
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    number = 12
    number2 = 2
    num = 0
    while True:
        try:
            ass.dell("Pic a number in between 2 and 12")
            i_num = int(input("\n"))
            if i_num > number:
                raise ValueTooLargeError
            elif i_num < number2:
                raise ValueTooSmallError
            num = i_num
            break
        except ValueTooSmallError:
            ass.dell("Do you not know how to count? that's too small")
            print()
        except ValueTooLargeError:
            ass.dell("Do you not know how to count? that's too big")
            print()
        sumb= rand + rand2
        if i_num == sumb:
            ass.dell("Wow! You won two coins")
            coi += 2
        elif rand == i_num or rand2 == i_num:
            ass.dell("Cool new kid, you won one coin")
            coi += 1
        else:
            ass.dell("Damn, you're bad at guessing")


def memory():
    n = random.randint(1, 99)
    ass.dell("Say a number inbetween 1 to 99: ")
    guess = input()
    while n != "guess":
        if guess < n:
            ass.dell("guess is low")
            ass.dell("different number")
            guess = input()
        elif guess > n:
            ass.dell("guess is high")
            ass.dell("what's an number from 1 to 99: ")
            guess = input()
        else:
            ass.dell("Damn, took you long enough!")
            break
        print



