#Zhicheng Zhu
#10/15/2024
#Name Generator

def food_name_generator():
    print ("Welcome to your food generator!")
    print ("Please answer these questions to find our your food!")
    ans = input("Hot(H) or Cold(C) ?")
    if ans == "H":
        ans = input("Food(F) or Drink(D) ?")
        if ans == "F":
            ans = input("Heat(He) or Oil(O) ?")
            if ans == "He":
                print("Your food is Pizza!")
            else:
                print("Your food is Donut!")
    if ans == "D":
        ans = input("Nutty(N) or Sweet(S) ?")
        if ans == "N":
            print("Your food is Coffee!")
        else:
            print("Your food is Soup!")
    if ans == "C":
        ans = input("Smooth(Sm) or Soft(So) ?")
        if ans == "Sm":
            ans = input("Grainy(G) or Creamy(Cr) ?")
            if ans == "G":
                print("Your food is Ice cream!")
            else:
                print("Your food is Smoothie!")
    if ans == "So":
        ans = input("Chewy(Ch) or Runny(Ru) ?")
        if ans =="Ch":
            print("Your food is Jello!")
        else:
            print("Your food is Yogurt!")
food_name_generator()
