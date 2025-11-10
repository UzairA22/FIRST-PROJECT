# CREATING A ROCK ,PAPER ,SCISSOR GAME

import random

# 1 for rock 
# -1 for paper
# 0 for scissor

print("ROCK,PAPER,SCISSOR:")
print('''
      Enter r for rock.
      Enter p for paper.
      Enter s for scissor.
      ''')

computer = random.choice([0,1,-1])

youin = input("Enter your choice:")
youdict = {
    "r" : 1,
    "p" : -1,
    "s" : 0
}
reversedict = {
    1 : "rock",
    -1 : "paper",
    0 : "scissor"
}
you = youdict[youin]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if (computer == you):
    print("it is a draw")

else:
    if (computer == 1 and you == -1):
        print("You win")

    elif (computer == 1 and you == 0):
        print("Computer wins")

    elif (computer == -1 and you == 0):
        print("You wins")

    elif (computer == -1 and you == 1):
        print("Computer wins")

    elif (computer == 0 and you == 1):
        print("You wins")            

    elif (computer == 0 and you == -1):
        print("Computer wins")    

    else :
        print("something went wrong")    

