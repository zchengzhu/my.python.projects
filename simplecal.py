#Zhicheng Zhu
#11/19/2024
#Simple Calculator

#Init
#Functions
#Adds num1 + num 2 and prints the results
def add (num1, num2):
    print(num1 + num2) #Code
def sub (num1, num2):
    print(num1 - num2)
def mul (num1, num2):
    print(num1 * num2)
def div (num1, num2):
    print(num1 / num2)

def simple_calculator():
    while True:
        print("Welcome Preschoolers to Simple Calculator")
        print("Please choose an operation: ")
        print("""1. Addition
2.Subtraction
3.Multiplication
4.Division
5.Quit""")
        operation = int(input("1-5 :"))
        if operation == 1:
            add1 = int(input("Enter first number: "))
            add2 = int(input("Enter second number: "))
            add(add1,add2)
        if operation == 2:
            sub1 = int(input("Enter first number: "))
            sub2 = int(input("Enter second number: "))
            sub(sub1,sub2)
        if operation == 3:
            mul1 = int(input("Enter first number: "))
            mul2 = int(input("Enter second number: "))
            mul(mul1,mul2)
        if operation == 4:
            div1 = int(input("Enter first number: "))
            div2 = int(input("Enter second number: "))
            div(div1,div2)
        if operation == 5:
            break
    print("Goodbye...")
#Main
simple_calculator()
