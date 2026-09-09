while True:

    print("\n----- MENU -----")
    print("1. Say Hello")
    print("2. Say Bye")
    print("3. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Hello Ganesh!")

    elif choice == 2:
        print("Bye Ganesh!")

    elif choice == 3:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")