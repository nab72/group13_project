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
        
if __name__ == "__main__":
    play_game()