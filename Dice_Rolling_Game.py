#Loop
    # Ask:user for dice rolling?
    #     if yes
    #         generate any random number
    #     if no
    #         print thank you message
    #         terminate
    #     else
    #         print invalid input


import random

while True:
    dice_roll=input("Do you want to roll the dice? (Y/N):")
    dice_ans=dice_roll.casefold()
    if(dice_ans == "y"):
        dice1=random.randint(1, 6)
        dice2=random.randint(1, 6)
        print("Dice1:",dice1)
        print("Dice2:",dice2)
    elif(dice_ans == "n"):
        print("Thanks for playing game")
        break
    else:
        print("Invalid Input")



