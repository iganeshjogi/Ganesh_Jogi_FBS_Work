while True:

    print("\n------ Calculator ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        print("Addition =", num1 + num2)

    elif choice == 2:

        num1 = int(input("Enter First Number: "))
        num2 = int(input("Enter Second Number: "))

        print("Subtraction =", num1 - num2)

    elif choice == 3:

        print("Thank You")
        break

    else:

        print("Invalid Choice")