# defining the necessary functions needed: add, sub, mul, div
# print the option to the user
# do not forget to ask for the values!!
# call the functions!!!
# add while loop to continue the program until the user decides to exit.

def add(a, b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul (a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div (a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")



while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")

    choice = input("input of your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Put The First Number: "))
        b = int(input("Put The Second Number: "))
        add(a,b)

    elif choice == "b" or choice == "B":
        print("Subscription")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        sub (a,b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        mul (a,b)

    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input First Number: "))
        b = int(input("Input Second Number: "))
        div (a,b)

    elif choice == "e" or choice == "E":
        print("It's Done.")
        quit()