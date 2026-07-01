# Ask:user for dice rolling?
#     if yes
#         generate any random number
#     if no
#         print thank you message
#         terminate
#     else
#         print invalid input

print(help(str.casefold))
import random
import builtins.str

while True:
    dice_roll=input("You want to Roll The Dice?(Y/N)")
    dice_ans=dice_roll.casefold()
    if(dice_ans == "Y"):
        no=random.randint(1, 7)
        print("(",no,")")
    elif(dice_ans == "N"):
        print("Thanks for playing game")
        break
    else:
        print("Invalid Input")



