import random
def hangman():
    word=random.choice(["pokemon","digimon","doremon"])
    userguess=" "
    turns=10
    while len(word)>0:
        main=""
        for i in word:
            if i in userguess:
                main=main+i
            else:
                main=main+" "+"_"

        if main==word:
            print(word)
            print("YOU WIN")

            break

        print("guess the word",main)
        guess=input()
        userguess=userguess+guess

        if guess not in word:
            turns=turns-1
            if turns==9:
                print("nine turns left")
            if turns==8:
                print("8 turns left")
            if turns==7:
                print("7 turns left")
            if turns==6:
                print("6 turns left")
            if turns==5:
                print("5 turns left")
            if turns==4:
                print("4 turns left")
            if turns==3:
                print("3 turns left")
            if turns==2:
                print("2 turns left")
            if turns==1:
                print("1 turn left")
            if turns==0:
                print("YOUR CHARACTER IS DEAD")
                break






name=input("enter your name")
print("Welcome to hangman game",name)
hangman()
