import random
x="y"
while x=="y":
    a=random.randint(1,6)
    if a==1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")

    elif a==2:
        print("---------")
        print("|       |")
        print("| 0  0  |")
        print("|       |")
        print("---------")

    elif a==3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")

    elif a==4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")

    elif a==5:
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
    x=input("do you want to continue? y/n ")
