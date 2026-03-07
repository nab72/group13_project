import random

def play_game():
    options = ["rock","paper","scissors"]
    
    while True:
        player = input("Enter Rock, Paper, or Scissors (or 'q' to quit): ").lower()
        
        if player == 'q':
            break
        if player not in options:
            print("Invalid input, try again.")
            continue
            
        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

play_game()