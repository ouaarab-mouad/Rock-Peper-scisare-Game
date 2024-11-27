import random

def get_user_choice():
    user_choice = input("dkhal hajra, waraka, ola mkas: ")
    return user_choice

def get_computer_choice():
    choices = ["hajra", "waraka", "mkas"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "ta3adol!"
    elif user_choice == "hajra" and computer_choice == "mkas":
        return "rbahti !"
    elif user_choice == "waraka" and computer_choice == "hajra":
        return "rbahti !"
    elif user_choice == "mkas" and computer_choice == "waraka":
        return "rbahti !"
    else:
        return "l pici li rbah!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
play_game()