import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    
    print("Welcome to Advanced Rock Paper Scissors!")
    
    while True:
        player_choice = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if player_choice == 'q':
            break
        if player_choice not in choices:
            print("Invalid choice, please try again.")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        print(f"Score: You {player_score} - {computer_score} Computer")

    print(f"\nFinal Score: You {player_score} - {computer_score} Computer")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
