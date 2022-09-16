import random
import time
from time import sleep

rock = "rock"
paper = "paper"
scissors = "scissors"

print("Welcome to Rock, Paper, Scissors!")
print("The game is pretty simple, you choose rock, paper, or scissors.")

time.sleep(1)
print("rock, paper or scissors? (Case sensitive)")

# Player 1
player1 = input()

# Player 2
random.randint(1, 3)
player2 = random.choice(["rock", "paper", "scissors"])
print("Player 2 chose " + player2)

# Rock, paper, scissors
if player1 == rock and player2 == scissors:
    print("Player 1 wins!")
elif player1 == scissors and player2 == paper:
    print("Player 1 wins!")
elif player1 == paper and player2 == rock:
    print("Player 1 wins!")
elif player1 == scissors and player2 == rock:
    print("Player 2 wins!")
elif player1 == rock and player2 == paper:
    print("Player 2 wins!")
elif player1 == paper and player2 == scissors:
    print("Player 2 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Invalid input!")
    print("Please try again.")

