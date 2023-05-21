import random
def check_val(r):
    if r==1:
        val='rock'
    elif r==2:
        val='paper'
    else:
        val='scissors'
    return val
    
def evaluate(n):
    r=random.randint(1,4)
    val=check_val(r)
    if (n==1 and r==2) or(n==2 and r==3) or (n==3 and r==1):
        print("computer choice: ",val)
        print("you lose")
    elif (n==1 and r==1) or(n==2 and r==2) or (n==3 and r==3):
        print("computer choice: ",val)
        print("Draw!")
    else:
        print("computer choice: ",val)
        print("you win")

print("(1)rock (2)paper (3)scissors")
n=int(input("enter any number:"))
print("your choice: ",check_val(n))
evaluate(n)
