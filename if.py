'''
Created on Jan 27, 2019

@author: Aaron
'''
spritul=input("do you want to see a spritul? y/n:")
if spritul=="y":
    print ("working.......")
    import turtle 
    t=turtle.Pen()
    t.width(2)
    for y in range(100):
        t.forward(y*2)
        t.left(89)
        for y in range(10):
            t.right(45)
            t.forward(y*2)
            t.back(y*y/y)
            


             
print("MUA")

    
    
    