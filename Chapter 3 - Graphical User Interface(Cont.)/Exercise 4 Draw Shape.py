import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def draw_shape():
    shape = shape_var.get()
    # Default dimentions for the multitude of shapes
    width, height = 100, 100
    if shape in ['Rectangle', 'Oval']:
        width, height = 200, 100
    # Variable center coordinates and default ones
    x_center, y_center = 200, 200  #theeedefaults
    if coord_entry.get():
        x_center, y_center = map(int, coord_entry.get().split(','))
    # Math for drawing from the center of the canvas
    x1 = x_center - width // 2
    y1 = y_center - height // 2
    x2 = x1 + width
    y2 = y1 + height
    if shape == 'Oval':
        canvas.create_oval(x1, y1, x2, y2)
    elif shape == 'Rectangle':
        canvas.create_rectangle(x1, y1, x2, y2)
    elif shape == 'Square':
        side = min(width, height)
        x2 = x1 + side
        y2 = y1 + side
        canvas.create_rectangle(x1, y1, x2, y2)
    elif shape == 'Triangle':
        canvas.create_polygon(x1, y1, x2, y1, (x1+x2)//2, y2)

def clear_canvas():
    canvas.delete('all')

# Setting dimensions for the canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Labels, shape selections and buttons
shape_var = tk.StringVar(root)
shape_var.set('Oval')

shape_option = tk.OptionMenu(root, shape_var, 'Oval', 'Rectangle', 'Square', 'Triangle')
shape_option.pack()

input_label = tk.Label(root, text="Enter center coordinates (x_center,y_center):\nFrom 0-400")
input_label.pack()

coord_entry = tk.Entry(root)
coord_entry.pack()

draw_button = tk.Button(root, text="Draw Shape", command=draw_shape)
draw_button.pack()

clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

root.mainloop()
