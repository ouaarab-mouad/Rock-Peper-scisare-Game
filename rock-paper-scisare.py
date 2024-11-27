import random

def get_user_choice():
    """Prompts the user for their choice and validates it."""
    choices = ["hajra", "waraka", "mkas"]
    while True:
        user_choice = input("Dkhal hajra, waraka, ola mkas: ").lower()
        if user_choice in choices:
            return user_choice
        print("Khitak! Sir 3awd dkhal hajra, waraka, ola mkas.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = ["hajra", "waraka", "mkas"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "Ta3adol!"
    win_conditions = {
        "hajra": "mkas",
        "waraka": "hajra",
        "mkas": "waraka"
    }
    if win_conditions[user_choice] == computer_choice:
        return "Rbahti!"
    return "L pici li rbah!"

def play_game():
    """Main function to play the game."""
    print("Mar7ba bik f l3ba hajra, waraka, mkas!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("\nBghiti t3awd l3ba? (yes/no): ").lower()
        if play_again != "yes":
            print("Shokran 3la l3ib, bslama!")
            break

if __name__ == "__main__":
    play_game()
