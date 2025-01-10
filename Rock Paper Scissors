#Zhicheng Zhu
#1/6/2024
#Rock Paper Scissors

import random

#Functions
#main

computer = 0
player = "0"

def RPS():
    global computer
    global player
    print("Welcome to Rock Paper Scisssors..!")
    print("Select Rock, Paper or scissors..") #Player(You) select one of these three options.
    computer = random.randint(1, 3)
    player = input("Selection: ") #String #Tells the program what the player(You) have selected.
    if computer == 1: #Computer options 
        computer = ("rock")
    print("Computer chosen rock..")
if computer == 2: #Computer options 
    computer == ("paper")
    print("Computer chosen paper..")
elif computer == 3: #Computer options 
    computer == ("scissors")
    print("Computer chosen scissors..")
if computer == "scissors" and player == "paper": #System outcome if option was chosen
    print("You lose..!")
if computer == "scissors" and player == "scissors": #System outcome if option was chosen
    print("You tied.. Try again!")
if computer == "rock" and player == "scissors": #System outcome if option was chosen
    print("You lose..!")
if computer == "rock" and player == "rock": #System outcome if option was chosen
    print("You tied.. Try again!")
if computer == "paper" and player == "scissors": #System outcome if option was chosen
    print("You lose..!")
if computer == "paper" and player == "paper": #System outcome if option was chosen
    print("You tied.. Try again!")
if computer == "paper" and player == "scissors": #System outcome if option was chosen
    print("You win..!")
if computer == "scissors" and player == "rock": #System outcome if option was chosen
    print("You win..!")
if computer == "rock" and player == "scissors": #System outcome if option was chosen
    print("You win..!")
    choice = input("Do you want to play again..?") #System will ask if you want to play again or not, if yes then game would repeat, if no then game will shut down
    if choice == "yes":
        print("Restarting...") #If yes game would repeat
        RPS()
    if choice == "no":
        break #If no then game would end
        print("Thanks for playing!")
RPS()
