'''
Created on Feb 16, 2019

@author: Aaron
'''

import random
import turtle
suits = ["clubs", "diamonds", "heart", "spades"]
fases = ["two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "jack", "queen", "king", "ace"]
playAgain = True;

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
        yourcard = yourcard - 2
        mycard += 1
    else:
        print("i won")
        yourcard += 1
        mycard = mycard - 2
    if mycard == 0:
        print("i lose you win")
    if yourcard == 0:
        print("i win you lose")
    pas = ""
    while pas != "y" and pas != "n":
        pas = input("Do you want to play again(y/n)?")
    if pas == "n":
        playAgain = False;

