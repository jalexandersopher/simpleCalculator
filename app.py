

while True:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")

    decision = input("Enter your selection: ")

    if decision == "q" or decision == "Q":
        break

    input1 = float(input("Enter your first number: "))
    input2 = float(input("Enter your second number: "))

    if decision == "1":
        print()
        print(input1, "+", input2, "=", (input1+input2))

    elif decision == "2":
        print()
        print(input1, "-", input2, "=", (input1-input2))

    elif decision == "3":
        print()
        print(input1, "*", input2, "=", (input1*input2))

    elif decision == "4":
        if input2 == 0.0:
            print()
            print("Cannot divide by 0")
        else:
            print()
            print(input1, "/", input2, "=", (input1/input2))

    else:
        print("Invalid selection")

    print()
    print()
    print()


