'''
Created on Feb 16, 2019

@author: Aaron
'''

import random
suits=["clubs","diamonds","heart","spades"]
fases = ["two","three","four","five","six","seven","eight"
         "nine","ten","jack","queen","king","ace"]
myace=random.choice(fases)
uts = random.choice(suits)
yourace=random.choice(fases)
youruts=random.choice(suits)
print("i get,",myace,"of,",uts)
print("you got",yourace,"of",youruts) 
if myace + uts == yourace + youruts:
    print("its a tie")
if myace + uts > yourace +youruts:
    print("i won")
else:
    print("you won")               
    
    
            