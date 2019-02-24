'''
Created on Feb 16, 2019

@author: Aaron
'''
import turtle
t = turtle.Pen
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
go = input("where do you want to go?")
if go == "up":
    up()
if go == "left":
    left()
if go == "right":
    right()
if go == "round":
    round()
else:
    print("this thing does not exist" )                                 

