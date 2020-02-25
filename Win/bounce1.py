'''
Created on 31, 

@author: aron Liu
'''
'''
Aaron's comments: 1.Why'd you sign your name as "aron" Liu? 2. On the
first line, you should add a semicolon and space (or even better, a 
newline!) after the text demanding input. That's good practice, my 100th 
middle name. 3. You should say what out of what to select. With a title
called "bounce1.py" nobody knows what to expect. Don't worry about all
the tornadoes, alarms, etc. Those are "easter eggs".
'''
le = input("select one")
while le=="alarm":
    print("its just a dream! wake up@#$#%@#$%$%#$")
    print("now your console gone completly wrong!")
if le=="tornado":
    print("ATTENTION! DISASTER WILL COME IN 1...SECOND!")
    print("i select alarm!you lose!!!!!!!!!!!!!!!!!!!!!!!!!!")
    quit()
if le == "scissors":
    print("i select rock! ya los!")
if le == "rock":
    print("supercalifragilisticexpalidocius! youlose i choose tornado!!!!! ")
if le == "paper":
    print("i choose scissor!yer chance was bad ")
if le != "rock" and le != "scissors" and le != "paper" and le!="tornado"and le!="alarm":
    print("SCRAM!")