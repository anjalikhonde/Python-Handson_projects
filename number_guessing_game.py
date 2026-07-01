import random

name=input("Enter your Name:")
while True:
    print("============================================")
    print("*********Lets start a game "+name+"**********")
    print("============================================")
    number = random.randint(1,150)

    while True:
        g_no = int(input("Enter Number:"))
        if g_no < 1 or g_no > 150:
            print("Invalid number")
        elif g_no < number :
            print("Too Low")    
        elif g_no > number :
            print("Too High")
        else:
            print("--------------------------------------")
            print("===========Number Found!!!============")
            print("--------------------------------------")
            break

    choice= input("you want to play one more round(Y/N):")
    final_choice = choice.casefold()
    if final_choice == "y":
          continue
    elif final_choice == "n":
        print("*************Thanks for playing game***************")
        print("Come back again......")
        break


    