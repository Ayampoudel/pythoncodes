import random
print("This is a dice stimulator")

x=random.randint(1,6)
if x==1:
    print("---------")
    print("|       |")
    print("|   0   |")
    print("|       |")
    print("---------")

elif x==2:
    print("---------")
    print("|       |")
    print("| 0  0  |")
    print("|       |")
    print("---------")

elif x==3:
    print("---------")
    print("|   0   |")
    print("|   0   |")
    print("|   0   |")
    print("---------")

elif x==4:
    print("---------")
    print("| 0   0 |")
    print("|       |")
    print("| 0   0 |")
    print("---------")

elif x==5:
    print("---------")
    print("| 0    0|")
    print("|   0   |")
    print("|0     0|")
    print("---------")

else:
    print("---------")
    print("|0 0 0  |")
    print("|       |")
    print("|0 0 0  |")
    print("---------")


def function(roll):
    if roll=='y':
        x=random.randint(1,6)
        if x==1:
            print("---------")
            print("|       |")
            print("|   0   |")
            print("|       |")
            print("---------")

        elif x==2:
            print("---------")
            print("|       |")
            print("| 0  0  |")
            print("|       |")
            print("---------")

        elif x==3:
            print("---------")
            print("|   0   |")
            print("|   0   |")
            print("|   0   |")
            print("---------")

        elif x==4:
            print("---------")
            print("| 0   0 |")
            print("|       |")
            print("| 0   0 |")
            print("---------")

        elif x==5:
            print("---------")
            print("| 0    0|")
            print("|   0   |")
            print("|0     0|")
            print("---------")

        else:
            print("---------")
            print("|0 0 0  |")
            print("|       |")
            print("|0 0 0  |")
            print("---------")

    elif roll=='n':
        print("Thanks for playing")

    elif(roll!='y' and roll!='n'):
        print("Couldn't recognize character")


turn=1
while(turn!=0):
    roll=input("Enter y to roll again or n to stop")
    if roll=='y':
        function(roll)
        turn=1
    elif roll=='n':
        print("Thanks for playing")
        turn=0
    else:
        print("Wrong character")
        turn=0
