import random

def get_user_choice():
    print("Enter your choice: Rock, Paper, or Scissors")
    user_choice = input().capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input().capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    print(f"\nYou chose {user_choice}.")
    print(f"Computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def print_scores(user_score, computer_score):
    print(f"Your Score: {user_score} | Computer Score: {computer_score}\n")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "You" in result:
            user_score += 1
        elif "Computer" in result:
            computer_score += 1

        print_scores(user_score, computer_score)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
