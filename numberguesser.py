#Zhicheng Zhu
#11/11/2024
#Number Guesser
usernumber = int(input("Hello, Welcome to Guess the Number!" + "  " + "Please Guess a Number 0 through 10 to win a Prize!"))
import random
actualnumber = random.randint(0,10)
#Make sure both variables are integers
def number_guesser():
    if actualnumber == usernumber:
        print("You are it correct!")
        print("Here is your Prize!")
    elif actualnumber < usernumber:
        print("You got it wrong!" + " " + "it's " " " + str(y))
        print("Try again!")

number_guesser()

