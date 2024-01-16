import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Arithmetic Operations")

# Class for arithmetic operations
class ArithmeticOperations:
    def __init__(self):
        self.result = 0  

    # Method to calculate result
    def calculate(self, operation, num1, num2):
        if operation == 'Add':
            self.result = num1 + num2  
        elif operation == 'Subtract':
            self.result = num1 - num2  
        elif operation == 'Multiply':
            self.result = num1 * num2  
        elif operation == 'Divide':
            if num2 != 0:
                self.result = num1 / num2  
            else:
                self.result = 'Error: Division by zero'
        
        return self.result 

# Func to calculate result
def calculate_result():
    num1 = float(num1_entry.get())  # First number from entry 1
    num2 = float(num2_entry.get())  # 2nd from entry 2
    operation = operation_combobox.get()  # Operation from combobox
    result = arithmetic_operations.calculate(operation, num1, num2)  # Calculate result
    result_label.config(text = str(result))  # Show result

arithmetic_operations = ArithmeticOperations()  # Arithmetic operations object

# Labels, entries, and combobox for numbers and operation
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(column=0, row=0)
num1_entry = tk.Entry(root)
num1_entry.grid(column=1, row=0)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(column=0, row=1)
num2_entry = tk.Entry(root)
num2_entry.grid(column=1, row=1)

operation_label = tk.Label(root, text="Operation:")
operation_label.grid(column=0, row=2)
operation_combobox = ttk.Combobox(root, values=["Add", "Subtract", "Multiply", "Divide"])
operation_combobox.grid(column=1, row=2)

# Button to calculate result
calculate_button = tk.Button(root, text="Calculate", command=calculate_result)
calculate_button.grid(column=0, row=3)

# Label to show result
result_label = tk.Label(root, text="")
result_label.grid(column=1, row=3)

root.mainloop()
