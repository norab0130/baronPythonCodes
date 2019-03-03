'''
Created on Jan 31, 2019

@author: Aaron Liu
'''
import random
dice=[0,0,0,0,0]
for i in range(5):
    dice[i]= random.randint(1,6)
print("you rolled ",dice)
dice.sort()
if dice[0] == dice[4]:
    print("yahitzee!")
if dice[0] == dice[3] or dice[1] == dice[4]:
    print("four of a kind!")
if dice[0]== dice[2] or dice[1]==dice[3] or dice[2]== dice[4]:
    print("three of a kind")    