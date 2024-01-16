import tkinter as tk

root = tk.Tk()

# Student class with grade calculation and display methods
class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name  
        self.mark1 = mark1  
        self.mark2 = mark2  
        self.mark3 = mark3  

    # Method to calc grade
    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3  # Average grade

    # Method to display student details
    def display(self):
        return f"Student Name: {self.name}, Grade Average: {self.calcGrade()}" 

# Func to submit details and display result
def submit():
    name = name_entry.get() 
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get()) # Marks from entry
    mark3 = int(mark3_entry.get())
    student = Students(name, mark1, mark2, mark3) # Student object
    result_label.config(text=student.display()) # Display details

# Labels and entries for name and marks
name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)  
name_entry.pack()

mark1_label = tk.Label(root, text="Mark 1")
mark1_label.pack()
mark1_entry = tk.Entry(root)  
mark1_entry.pack()

mark2_label = tk.Label(root, text="Mark 2")
mark2_label.pack()
mark2_entry = tk.Entry(root) 
mark2_entry.pack()

mark3_label = tk.Label(root, text="Mark 3")
mark3_label.pack()
mark3_entry = tk.Entry(root) 
mark3_entry.pack()

# Submit button and result label
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
