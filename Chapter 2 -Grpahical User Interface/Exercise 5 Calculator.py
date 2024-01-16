import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

# Main function
def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation.get() == "Addition":
            result.set(num1 + num2)
        elif operation.get() == "Subtraction":
            result.set(num1 - num2)
        elif operation.get() == "Multiplication":
            result.set(num1 * num2)
        elif operation.get() == "Division":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Division by zero")
        elif operation.get() == "Modulo Division":
            if num2 != 0:
                result.set(num1 % num2)
            else:
                result.set("Error: Modulo by zero")
    except ValueError:
        result.set("Error: Invalid input")

# Entry fields
entry_num1 = tk.Entry(root, width=15)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=15)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Drop down for operations
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo Division"]
operation = tk.StringVar()
operation.set(operations[0])  # Default operation
dropdown = tk.OptionMenu(root, operation, *operations)
dropdown.grid(row=0, column=2, padx=10, pady=10)

# Button for operation
calculate_button = tk.Button(root, text="Calculate", command=perform_operation)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

# Display result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
