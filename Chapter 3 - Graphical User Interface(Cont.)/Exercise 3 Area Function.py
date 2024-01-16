import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Area Calculator")

def calculate_circle():
    r = float(circle_radius.get())
    area = 3.14 * (r ** 2)
    circle_result.config(text = "Area is: " + str(area))

def calculate_square():
    s = float(square_side.get())
    area = s ** 2
    square_result.config(text = "Area is: " + str(area))

def calculate_rectangle():
    w = float(rectangle_width.get())
    h = float(rectangle_height.get())
    area = w * h
    rectangle_result.config(text = "Area is: " + str(area))

# Tabs
tabs = ttk.Notebook(root)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

tabs.add(tab1, text="Circle")
tabs.add(tab2, text="Square")
tabs.add(tab3, text="Rectangle")

# Cirle
ttk.Label(tab1, text="Radius:").pack()
circle_radius = tk.StringVar()
circle_entry = ttk.Entry(tab1, textvariable=circle_radius).pack()
circle_button = ttk.Button(tab1, text="Calculate Area", command=calculate_circle).pack()
circle_result = ttk.Label(tab1, text="")
circle_result.pack()

# Square
ttk.Label(tab2, text="Side Length:").pack()
square_side = tk.StringVar()
square_entry = ttk.Entry(tab2, textvariable=square_side).pack()
square_button = ttk.Button(tab2, text="Calculate Area", command=calculate_square).pack()
square_result = ttk.Label(tab2, text="")
square_result.pack()

# Rectangle
ttk.Label(tab3, text="Width:").pack()
rectangle_width = tk.StringVar()
rectangle_width_entry = ttk.Entry(tab3, textvariable=rectangle_width).pack()
ttk.Label(tab3, text="Height:").pack()
rectangle_height = tk.StringVar()
rectangle_height_entry = ttk.Entry(tab3, textvariable=rectangle_height).pack()
rectangle_button = ttk.Button(tab3, text="Calculate Area", command=calculate_rectangle).pack()
rectangle_result = ttk.Label(tab3, text="")
rectangle_result.pack()

tabs.pack(expand=1, fill='both')

root.mainloop()
