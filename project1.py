import random
def gameWin(comp,you):
    if comp == you :
        return None
    elif comp == 's':
        if you == 'w':
            return False 
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True        
    
print(" Comp turn : Snake(s) Water(w) or Gun(g) ?")
randomNo = random.randint(1,3)
if randomNo == 1:
     comp = 's'
elif randomNo == 2:
     comp = 'w'
elif randomNo == 3:
     comp = 'g'

you = input(" Your turn : Snake(s) Water(w) or Gun(g) ?\n")
print(f"you choose {you}")
print(f"computer choose {comp}")
a = gameWin(comp,you)
if a == None:
    print("It's a tie !")
elif a:
    print("You won !")
else:
    print("You lose !")
