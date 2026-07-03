import random

emojis = {"r":"\U0001F9A8" , "p":"\U0001F4C4", "s":"\u2702"}
choices = ("r","p","s")

name=input("Enter your Name:")
game_running = True
while game_running:
    ...
    print("\n🎮" + "=" * 44 + "🎮")
    print(f"🎉 Welcome, {name}! Let's Start the Game! 🚀")
    print("🪨 📄 ✂️  Rock • Paper • Scissors  ✂️ 📄 🪨")
    print("🎮" + "=" * 44 + "🎮")
    user_choice = input("Choose Rock,Paper,Scissor(r,p,s):").lower()

    if user_choice not in choices:
        print("❌ Invalid choice!")
        print("👉 Please choose only: r (Rock), p (Paper), or s (Scissors).")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("🎉🎉 Congratulations! You Win! 🏆🥳")
    else:
        print("😢 You Lose! Better luck next time! 💔")

    while True:
        choice1= input("you want to play one more round(Y/N):")
        final_choice = choice1.casefold()
        if final_choice == "y":
            break
        elif final_choice == "n":
            print("\n🎮══════════════════════════════════════🎮")
            print("🙏 Thanks for Playing!")
            print("❤️ Hope you had fun!")
            print("👋 See you again soon!")
            print("🎮══════════════════════════════════════🎮")
            exit()            
        else:
            print("❌ Invalid input! Please enter Y or N.")
            continue
   