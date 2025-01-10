#Zhicheng Zhu
#10/15/2024
#Name Generator

def food_name_generator():
    print ("Welcome to your food generator!")
    print ("Please answer these questions to find our your food!") #Type in the answer for these questions
    ans = input("Hot(H) or Cold(C) ?") #Select which option you prefer
    if ans == "H":
        ans = input("Food(F) or Drink(D) ?") #Select which option you prefer
        if ans == "F":
            ans = input("Heat(He) or Oil(O) ?") #Select which option you prefer
            if ans == "He":
                print("Your food is Pizza!")  #System outcome to find what food you would like
            else:
                print("Your food is Donut!")  #System outcome to find what food you would like
    if ans == "D":
        ans = input("Nutty(N) or Sweet(S) ?") #Select which option you prefer
        if ans == "N":
            print("Your food is Coffee!")  #System outcome to find what food you would like
        else:
            print("Your food is Soup!")  #System outcome to find what food you would like
    if ans == "C":
        ans = input("Smooth(Sm) or Soft(So) ?") #Select which option you prefer
        if ans == "Sm":
            ans = input("Grainy(G) or Creamy(Cr) ?") #Select which option you prefer
            if ans == "G":
                print("Your food is Ice cream!") #System outcome to find what food you would like
            else:
                print("Your food is Smoothie!") #System outcome to find what food you would like
    if ans == "So":
        ans = input("Chewy(Ch) or Runny(Ru) ?")#Select which option you prefer
        if ans =="Ch":
            print("Your food is Jello!") #System outcome to find what food you would like
        else:
            print("Your food is Yogurt!") #System outcome to find what food you would like
food_name_generator() 
