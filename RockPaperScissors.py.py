#Zhicheng Zhu
#1/6/2024
#Rock Paper Scissors

import random

#Functions
#main

#Step 1: Player selects an option
#Step 2: Making a selection for the computer
computer = 0
player = "0"

def RPS():
    global computer
    global player
    print("Welcome to Rock Paper Scisssors..!")
    print("Select Rock, Paper or scissors..")
    computer = random.randint(1, 3)
    player = input("Selection: ") #String
    if computer == 1:
        computer = ("rock")
    print("Computer chosen rock..")
if computer == 2:
    computer == ("paper")
    print("Computer chosen paper..")
elif computer == 3:
    computer == ("scissors")
    print("Computer chosen scissors..")
if computer == "scissors" and player == "paper":
    print("You lose..!")
if computer == "scissors" and player == "scissors":
    print("You tied.. Try again!")
if computer == "rock" and player == "scissors":
    print("You lose..!")
if computer == "rock" and player == "rock":
    print("You tied.. Try again!")
if computer == "paper" and player == "scissors":
    print("You lose..!")
if computer == "paper" and player == "paper":
    print("You tied.. Try again!")
if computer == "paper" and player == "scissors":
    print("You win..!")
if computer == "scissors" and player == "rock":
    print("You win..!")
if computer == "rock" and player == "scissors":
    print("You win..!")

#Step 3: Determine the outcome
RPS()
