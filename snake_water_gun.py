import random
def playthegame(comp,user):
    if comp==user:
        return 0
    elif comp==2 and user==0:
        return -1
    elif comp==0 and user==1:
        return -1
    elif comp==1 and user==2:
        return -1
    else:
        return 1

comp=random.randint(0,2)
user=int(input("Enter 0 for snake, 1 for water, 2 for gun: "))
score=playthegame(comp,user)
print(f"Your turn: {user}\nComp turn: {comp}")
if score==0:
    print("It's draw")
elif score==1:
    print("You won")
else:
    print("You lose")    

    