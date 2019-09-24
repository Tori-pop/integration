#       Victoria Poplawski
#       Text based advanture game


print("Hey, my name is Chris")
name = raw_input("what's your name?\n")
print("Nice to meet you, " + name)
age = raw_input("I'm 13. \nHow old are you?\n")
ageCal = int(age) - 13

if age == 13:
    print("Then we're the same age")
else:
    print("So we are " + str(abs(ageCal))+ " years apart")
print("So... Do you want to go to the park or if your brave we can go somewhere cooler?")
firstBranch = raw_input("Type 'x' if you feel brave\n")
#       This is the first story branch
if firstBranch == "x" or firstBranch == "X":
    print("Awesome then lets go to the Sunken House")
else:
    print("Fine, we'll find something boring to do")
    print("I say we toss a coin.")
    flip = coinFlip()

#       Coin Flip function
def coinFlip():
    coin = ('heads', 'tails')
    flip = random.choice(coin)
    your_choice = input("heads or tails")
    if your_choice == flip:
        print('It landed on {}. You win'.format(flip))
    else:
        print("Uh oh. Coin landed on {}. Guess we're going to the back house".format(flip))































































