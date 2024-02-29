#Rock Paper Scissor Game

import random

options = ("rock", "paper", "scissor")
running = True

while running:
    
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter your choice (rock, paper, scissor):")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Match is Tie!")
    elif player == "Rock" and computer == "Scissor":
        print("You Win!")
    elif player == "Paper" and computer == "Rock":
        print("You Win!")
    elif player == "Scissor" and computer == "Paper":
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Play Again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing!")
