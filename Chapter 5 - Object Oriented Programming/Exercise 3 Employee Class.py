import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Employee class with set and get methods
class Employee:
    def setData(self, name, position, salary, id):
        self.name = name  
        self.position = position  
        self.salary = salary  
        self.id = id  

    # Method to get data
    def getData(self):
        return self.name, self.position, self.salary, self.id 

employees = []  # List to store employees

# Func to add employee
def add_employee():
    # Pointing to entries
    name = name_entry.get()  
    position = position_entry.get()  
    salary = salary_entry.get()  
    id = id_entry.get()  
    employee = Employee()  
    employee.setData(name, position, salary, id)  
    employees.append(employee)  
    messagebox.showinfo("Success", "Employee added successfully!")  

# Func to display employees
def display_employee():
    # Print header
    print(f"{'Name':<10}{'Position':<15}{'Salary':<10}{'ID':<5}")
    
    for employee in employees:
        name, position, salary, emp_id = employee.getData()
        # Print data in a tabular format
        print(f"{name:<10}{position:<15}{salary:<10}{emp_id:<5}")


# Labels and entries for name, position, salary, and id
name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)  
name_entry.pack()

position_label = tk.Label(root, text="Position")
position_label.pack()
position_entry = tk.Entry(root)  
position_entry.pack()

salary_label = tk.Label(root, text="Salary")
salary_label.pack()
salary_entry = tk.Entry(root)  
salary_entry.pack()

id_label = tk.Label(root, text="ID")
id_label.pack()
id_entry = tk.Entry(root)  
id_entry.pack()

# Add and display buttons
add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.pack()

display_button = tk.Button(root, text="Display Employees", command=display_employee)
display_button.pack()

root.mainloop()
