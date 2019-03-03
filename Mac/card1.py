'''
Created on Feb 16, 2019

@author: Aaron
'''

import random
suits = ["clubs", "diamonds", "heart", "spades"]
fases = ["two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "jack", "queen", "king", "ace"]
playAgain = True;
mC = 0;
yC = 0;
while playAgain:
    myace = random.choice(fases)
    uts = random.choice(suits)
    yourace = random.choice(fases)
    youruts = random.choice(suits)
    mycard = 50
    yourcard = 50
    print("i get", myace, "of", uts)
    print("you got", yourace, "of", youruts) 
    if myace + uts == yourace + youruts:
        print("its a tie")
        mycard = mycard - 1
        yourcard = yourcard - 1
    if myace + uts > yourace + youruts:
        print("you won")
        yC += 1
    else:
        print("i won")
        mC += 1
    if mycard == 0:
        print("i lose you win")
    if yourcard == 0:
        print("i win you lose")
    pas = ""
    while pas != "y" and pas != "n":
        pas = input("Do you want to play again(y/n)?")
    if pas == "n":
        playAgain = False;
print("SCOREBOARD:")
print("WE HAVE PLAYED")
print(yC+mC)
print("ROUNDS")
choices = [0, 1];
order = 0
if order == random.choice(choices):
    print("MY SCORE ISSSSSSSSSSSSS...")
    print(str(mC) + "!")
    print("AAAAAAAAAAAAAND...")
    print("YOUR")
    print("SCORE")
    print("ISSSSSSSSSSS...")
    print("suspense")
    print("suspense")
    print("suspense")
    print("YOUR SCORE IS " + str(yC) + "!")
else:
    print("YOUR SCORE ISSSSSSSSSSSSS...")
    print(str(yC) + "!")
    print("AAAAAAAAAAAAAND...")
    print("MY")
    print("SCORE")
    print("ISSSSSSSSSSS...")
    print("suspense")
    print("suspense")
    print("suspense")
    print("MY SCORE IS " + str(mC) + "!")
print("I WIN!!!!YAYYYAYÅÁAYAYAYAY!" if mC > yC else "you win............nooooooooooo")
print("Anyways,Goodbye!")
