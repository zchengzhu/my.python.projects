#3/19
#Create Task

import time
import random
FlyingLong = ["albatross", "crane", "flamingo", "pelican", "crane fly", "dragonfly", "jacana", "ibex", "bat", "flying squirrel"]

FlyingShort = ["Hummingbird", "Bumblebee", "Swallow ", "Dragonfly ", "Finch", "Chickadee", "Moth", "Kingfisher", "Nighthawk", "Pipistrelle Bat"]

NonLong = ["Giraffe", "Camel", "Ostrich", "Gazelle", "Horse ", "Kangaroo", "Elephant", "Moose", "Llama", "Elk"]

NonShort = ["Dachshund", "Corgi", "Penguin", "Turtle", "Hedgehog", "Bulldog", "Kangaroo Rat", "Pygmy Hippo", "Chinchilla", "Warthog"]

sFlyingLong = ["albatros", "grulla", "flamenco", "pelícano", "típula grulla", "libélula", "jacana", "íbice", "murciélago", "ardilla voladora"]

sFlyingShort = ["Colibrí", "Abejorro", "Golondrina", "Libélula", "Pinzón", "Carbonero", "Polilla", "Martín Pescador", "Choquete", "Murciélago Pipistrelle"]

sNonLong = ["Jirafa", "Camello", "Avestruz", "Gacela", "Caballo", "Canguro", "Elefante", "Alce", "Llama", "Venado"]

sNonShort = ["Perro salchicha", "Corgi", "Pingüino", "Tortuga", "Erizo", "Bulldog", "Rata canguro", "Hipopótamo pigmeo", "Chinchilla", "Facoquero"]


def tf():
        global FlyingLong
        global FlyingShort
        global NonLong
        global NonShort
        while True:
                print("Welcome to your favorite animal picker!")
                print("""
        Please choose an option:
                A) Flying Long Leg Animal
                B) Flying Short Leg Animal
                C) Non Flying Long Leg Animal
                D) Non Flying Short Leg Animal
                E) Quit
                                   """)
                user_input = str(input("(A,B,C,D,E) "))
                if user_input.upper() == "A":
                        for i in range(3):
                                print("Printing..")
                                time.sleep(2)
                        print(" ")
                        print("These are some flying long leg animals")
                        for animal in (FlyingLong):
                                print(animal)
                        print("")
                        one = input("Do you want to spin for your chosen animal?: Y or N ")
                        if one.upper() == "Y":
                                random_one = random.choice(FlyingLong)
                                for i in range(3):
                                        print("Spinning..")
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_one)
                        if one.upper() == "N":
                                print(" ")

                elif user_input.upper() == "B":
                        for i in range(3):
                                print("Printing..") 
                                time.sleep(2)
                        print(" ")
                        print("These are some flying short leg animals")
                        for animal in (FlyingShort):
                                print(animal) #Prints all the flying short legged animal options
                        print("")
                        two = input("Do you want to spin for your chosen animal?: Y or N ") #Asking if you want to spin for a chosen animal
                        if two.upper() == "Y": #Spins for a random flying short legged animal
                                random_two = random.choice(FlyingShort)
                                for i in range(3):
                                        print("Spinning..") #Shows a spinning command to simluate a random flying short legged animal is being chosen
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_two) #Shows your chosen random flying short legged animal
                        if two.upper() == "N": #Does nothing if selected N
                                print(" ")

                elif user_input.upper() == "C": #Option for non flying long leg animal
                        for i in range(3):
                                print("Printing..")#Shows a printing  command to simluate the code is printing
                                time.sleep(2)
                        print(" ")
                        print("These are some non flying long leg animals")
                        for animal in (NonLong):
                                print(animal) #Prints all the non flying long legged animal options
                        print("")
                        three = input("Do you want to spin for your chosen animal?: Y or N ") #Asking if you want to spin for a chosen animal
                        if three.upper() == "Y": #Spins for a random non flying long legged animal
                                random_three = random.choice(NonLong)
                                for i in range(3):
                                        print("Spinning..") #Shows a spinning command to simluate a random non flying long legged animal is being chosen
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_three) #Shows your chosen random non flying long legged animal
                        if three.upper() == "N":#Does nothing if selected N
                                print(" ")

                elif user_input.upper() == "D": #Option for non flying short leg animal
                        for i in range(3):
                                print("Printing..")#Shows a printing  command to simluate the code is printing
                                time.sleep(2)
                        print(" ")
                        print("These are some non flying short leg animals")
                        for animal in (NonShort):
                                print(animal) #Prints all the non flying short legged animal options
                        print("")
                        four = input("Do you want to spin for your chosen animal?: Y or N ") #Asking if you want to spin for a chosen animal
                        if four.upper() == "Y": #Spins for a random non flying short legged animal
                                random_four = random.choice(NonShort)
                                for i in range(3):
                                        print("Spinning..") #Shows a spinning command to simluate a random non flying short legged animal is being chosen
                                        time.sleep(2)
                                print("Your favorite animal is a " + random_four) #Shows your chosen random non flying short legged animal
                        if four == "N":#Does nothing if selected N
                                print(" ")

                elif user_input.upper() == "E": #Closes the animal picker
                        print("Quitting...")
                        break
                else:
                        print("Invalid option. Try again.") #Makes sure that there will be only one option for the answer choice to be seclected

def ff():
        global sFlyingLong
        global sFlyongShort
        global sNonLong
        global sNonShort
        while True:
                print("Bienvenido a tu recogedor de animales favorito!")
                print("""
        Por favor elige una opción:
               A) Animal volador de patas largas
                B) Animal volador de patas cortas
                C) Animal no volador de patas largas
                D) Animal no volador de patas cortas
                E) Renunciar
                                   """)
                user_input = str(input("(A,B,C,D,E) "))
                if user_input.upper() == "A":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales voladores de patas largas.")
                        for animal in (sFlyingLong):
                                print(animal)
                        print("")
                        one = input("¿Quieres girar para tu animal elegido?: Y or N ")
                        if one.upper() == "Y":
                                random_one = random.choice(sFlyingLong)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_one)
                        if one.upper() == "N":
                                print(" ")

                elif user_input.upper() == "B":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales voladores de patas cortas.")
                        for animal in (sFlyingShort):
                                print(animal)
                        print("")
                        two = input("¿Quieres girar para tu animal elegido?: Y or N ")
                        if two.upper() == "Y":
                                random_two = random.choice(sFlyingShort)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_two)
                        if two.upper() == "N":
                                print(" ")
                elif user_input.upper() == "C":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales de patas largas que no vuelan.")
                        for animal in (sNonLong):
                                print(animal)
                        print("")
                        three = input("¿Quieres girar para tu animal elegido??: Y or N ")
                        if three.upper() == "Y":
                                random_three = random.choice(sNonLong)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_three)
                        if three.upper() == "N":
                                print(" ")
                elif user_input.upper() == "D":
                        for i in range(3):
                                print("Impresión..")
                                time.sleep(2)
                        print(" ")
                        print("Estos son algunos animales de patas cortas que no vuelan.")
                        for animal in (sNonShort):
                                print(animal)
                        print("")
                        four = input("¿Quieres girar para tu animal elegido?: Y or N ")
                        if four.upper() == "Y":
                                random_four = random.choice(sNonShort)
                                for i in range(3):
                                        print("Hilado..")
                                        time.sleep(2)
                                print("Tu animal favorito es un " + random_four)
                        if four.upper() == "N":
                                print(" ")
                elif user_input.upper() == "E":
                        print("Dejar de fumar...")
                        break
                else:
                        print("Invalid option. Try again.")
def thef(language):
        if language == "English":
                tf()
        elif language == "Spanish":
                ff()
thef(input("What language do you what to do this in? English or Spanish "))
