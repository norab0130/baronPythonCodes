'''
Created on Jan 12, 2019

@author: Aaron
'''
import turtle
t=turtle.Pen()
t.speed(9)
turtle.bgcolor=("black")
colors=("red","yellow","blue","green")
for x in range(100):
    print(x%4,colors[x%4])
    t.color(colors[x%4])
    t.circle(x)
    t.left(92)