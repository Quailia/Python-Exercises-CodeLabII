import tkinter as tk
from math import pi

root = tk.Tk()
root.geometry("250x300")

# Shape class with input method
class Shape:
    def inputSides(self):
        self.sides = float(self.entry.get())  # Sides from entry

# Circle class with area method
class Circle(Shape):
    def area(self):
        return pi * self.sides * self.sides  # Area of circle

# Rectangle class with input and area methods
class Rectangle(Shape):
    def inputSides(self):
        self.length = float(self.entry1.get())  
        self.width = float(self.entry2.get())  

    def area(self):
        return self.length * self.width  # Area of rectangle

# Triangle class with input and area methods
class Triangle(Shape):
    def inputSides(self):
        self.base = float(self.entry1.get())  
        self.height = float(self.entry2.get())  

    def area(self):
        return 0.5 * self.base * self.height  # Area of triangle

# Func to calc area
def calculate_area():
    # Objects, entries and inputs
    if shape.get() == "Circle":
        circle = Circle()  
        circle.entry = entry  
        circle.inputSides()  
        result = circle.area()  # Calc area
    elif shape.get() == "Rectangle":
        rectangle = Rectangle()  
        rectangle.entry1 = entry1  
        rectangle.entry2 = entry2  
        rectangle.inputSides()  
        result = rectangle.area()  # Calc area
    elif shape.get() == "Triangle":
        triangle = Triangle()  
        triangle.entry1 = entry1  
        triangle.entry2 = entry2  
        triangle.inputSides()  
        result = triangle.area()  # Calc area
    
    result_label.config(text=f"The area of the {shape.get()} is {result}")  # Update label text

# Labels, entries, and buttons for shapes
label0 = tk.Label(root, text="NOTE:\n\nONLY input in the respectively\nlabeled entries per shape.\n")
label0.pack()

shape = tk.StringVar()
shapes = ["Circle", "Rectangle", "Triangle"]
shape.set(shapes[0])

option_menu = tk.OptionMenu(root, shape, *shapes)
option_menu.pack()

label = tk.Label(root, text="Radius for Circle")
label.pack()

entry = tk.Entry(root)  
entry.pack()

label1 = tk.Label(root, text="Length for Rectangle / Base for Triangle")
label1.pack()

entry1 = tk.Entry(root)  
entry1.pack()

label2 = tk.Label(root, text="Width for Rectangle / Height for Triangle")
label2.pack()

entry2 = tk.Entry(root)  
entry2.pack()

button = tk.Button(root, text="Calculate Area", command=calculate_area)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
