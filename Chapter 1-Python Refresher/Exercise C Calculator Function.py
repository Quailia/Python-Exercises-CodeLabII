def calculator():
    while True:
        print("Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        choice = int(input("Choose the operation (from 1 to 5): "))
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print("Result: ", num1 + num2)
        elif choice == 2:
            print("Result: ", num1 - num2)
        elif choice == 3:
            print("Result: ", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("Result: ", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == 5:
            print("Result: ", num1 % num2)
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

        another = input("Would you like to perform another calculation? (yes/no): ")
        
        if another.lower() != "yes":
            break

calculator()
