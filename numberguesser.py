#Zhicheng Zhu
#11/11/2024
#Number Guesser
usernumber = int(input("Hello, Welcome to Guess the Number!" + "  " + "Please Guess a Number 0 through 10 to win a Prize!")) 
import random
actualnumber = random.randint(0,10) #randomize the number the player(You) would have to guess
def number_guesser():
    if actualnumber == usernumber: #Makes system look if the number picked is equals to the player's(Yours) number
        print("You are it correct!") # System tells the player(You) if you're correct
        print("Here is your Prize!")
    elif actualnumber < usernumber: # Makes system look if the number picked is not equal to the player's(Yours) number
        print("You got it wrong!" + " " + "it's " " " + str(y)) #System tells the player(You) if your wrong
        print("Try again!")

number_guesser()

