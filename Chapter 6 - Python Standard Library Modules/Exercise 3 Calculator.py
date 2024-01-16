import operator

# Calculator function
def calculator():
    while True:
        print("Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Check greater number")
        print("Q. Quit")
        
        # Operations dictionary
        operations = {
            1: operator.add,  
            2: operator.sub,  
            3: operator.mul,  
            4: operator.truediv,  
            5: operator.mod,  
            6: operator.gt  
        }

        choice = input("Choose operation (from 1 to 6, or Q to quit): ").upper()  # Get choice

        if choice == 'Q':  
            print("Exiting...")
            break

        try:
            choice = int(choice)  # Convert choice to int
        except ValueError: 
            print("\nError. Enter a number or 'Q' to quit.\n") 
            continue  

        if choice not in operations:  
            print("\nError. Enter a number or 'Q' to quit.\n")  
            continue  

        num1 = float(input("Enter first number: "))  # Get num1
        num2 = float(input("Enter second number: "))  # Get num2

        result = operations[choice](num1, num2)  # Calculate result
        print(f"Result is {result}\n") 

calculator()  # Calling the function
