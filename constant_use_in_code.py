import random

# ==========================================================
# Rock Paper Scissors Game
# ==========================================================

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojis = {
    ROCK: "🪨",
    PAPER: "📄",
    SCISSORS: "✂️"
}

choices = tuple(emojis.keys())

# # ==========================================================
# # Get Player Name
# # ==========================================================
# def get_name():
#     name = input("Enter your Name: ")
#     return name


# # ==========================================================
# # Get User Choice
# # ==========================================================
# def get_user_choice(name):

#     print("\n🎮" + "=" * 44 + "🎮")
#     print(f"🎉 Welcome, {name}! Let's Start the Game! 🚀")
#     print("🪨 📄 ✂️  Rock • Paper • Scissors  ✂️ 📄 🪨")
#     print("🎮" + "=" * 44 + "🎮")

#     user_choice = input("Choose Rock, Paper, Scissors (r/p/s): ").lower()

#     return user_choice


# # ==========================================================
# # Validate User Choice
# # ==========================================================
# def invalid_choice(user_choice):

#     if user_choice not in choices:
#         print("❌ Invalid choice!")
#         print("👉 Please choose only: r (Rock), p (Paper), or s (Scissors).")
#         return False

#     return True


# # ==========================================================
# # Print Choices
# # ==========================================================
# def print_choices(user_choice):

#     computer_choice = random.choice(choices)

#     print(f"\nYou chose      : {emojis[user_choice]}")
#     print(f"Computer chose : {emojis[computer_choice]}")

#     return computer_choice


# # ==========================================================
# # Decide Winner
# # ==========================================================
# def game_logic(user_choice, computer_choice):

#     if user_choice == computer_choice:
#         print("🤝 It's a Tie!")

#     elif (
#         (user_choice == ROCK and computer_choice == SCISSORS) or
#         (user_choice == SCISSORS and computer_choice == PAPER) or
#         (user_choice == PAPER and computer_choice == ROCK)
#     ):
#         print("🎉🎉 Congratulations! You Win! 🏆🥳")

#     else:
#         print("😢 You Lose! Better luck next time! 💔")


# # ==========================================================
# # Play Again?
# # ==========================================================
# def end_of_the_game():

#     while True:

#         choice = input("\nDo you want to play another round? (Y/N): ").lower()

#         if choice == "y":
#             return True

#         elif choice == "n":
#             print("\n🎮══════════════════════════════════════🎮")
#             print("🙏 Thanks for Playing!")
#             print("❤️ Hope you had fun!")
#             print("👋 See you again soon!")
#             print("🎮══════════════════════════════════════🎮")
#             return False

#         else:
#             print("❌ Invalid input! Please enter Y or N.")


# # ==========================================================
# # Main Program
# # ==========================================================

# name = get_name()

# game_running = True

# while game_running:

#     user_choice = get_user_choice(name)

#     is_valid = invalid_choice(user_choice)

#     if not is_valid:
#         continue

#     computer_choice = print_choices(user_choice)

#     game_logic(user_choice, computer_choice)

#     game_running = end_of_the_game()