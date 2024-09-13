import random

option = ["rock", "paper", "scissors"]
guess = ""
repeat = ""
wins = 0
tries = 0

print("Rock, Paper, Scissors Game")
while True:
    if repeat == "n":
        print("=========Score=========")
        print(f"Tries: {tries}")
        print(f"Your total wins: {wins}")
        break
    else:
        answer = random.choice(option)
        guess = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if guess in option:
            if  guess == answer:
                print(f"Player: {guess}, Computer: {answer}")
                print("Draw")
            elif guess == "rock" and answer == "paper":
                print(f"Player: {guess}, Computer: {answer}")
                print("You lose")
            elif guess == "rock" and answer == "scissors":
                print(f"Player: {guess}, Computer: {answer}")
                print("You win")
                wins += 1
            elif guess == "paper" and answer == "rock":
                print(f"Player: {guess}, Computer: {answer}")   
                print("You win")
                wins += 1
            elif guess == "paper" and answer == "scissors":
                print(f"Player: {guess}, Computer: {answer}")
                print("You lose")
            elif guess == "scissors" and answer == "rock":
                print(f"Player: {guess}, Computer: {answer}")
                print("You lose")
            elif guess == "scissors" and answer == "paper":
                print(f"Player: {guess}, Computer: {answer}")
                print("You win")
                wins += 1
            tries += 1
        else:
            print("Invalid input")
        repeat = input("Would you like to play again? (y/n): ").lower()

        

