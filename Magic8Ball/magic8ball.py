import random
import sys
from time import sleep

answer1 = "Yes"
answer2 = "No"

def roll():
    #grab a random number
    random_number = random.randint(1,20)

    #print the random number
    print("The 8 ball is shaking...")
    sleep(1)
    print(" ")
    print(" ")

    #print the answer
    print(random.choice([answer1, answer2]))

    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

choice = input("Ask again? [y/n] >>> ")
if choice == "y":
    roll()   
elif choice == "n":
    exit()
else:
    "Invalid Choice, exiting"
    sleep(1)


print("This is the magic 8ball. Ask a yes/no question, and the python 8 ball with answer your query. What is your question?")
qa = input("> ")
if qa == "will thribhu get some bitches":
    print("idk, will jeff get some?")
else:
    roll()

