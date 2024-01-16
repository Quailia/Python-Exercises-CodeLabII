import tkinter as tk
from tkinter import font
import random

root = tk.Tk()
root.geometry("530x150")
root.title("Welcome App")

def get_random_font():
    # Can add as many more fonts as needed
    font_families = ["Arial", "Times New Roman", "Courier New", "Verdana", "Georgia", "Comic Sans MS"] 
    random_font_family = random.choice(font_families)
    random_font_size = random.randint(12, 24)  # Random font size between 12 and 24
    return font.Font(family=random_font_family, weight="normal", size=random_font_size)

def change_style_and_color():
    # Font styling
    new_font = get_random_font()
    welcome_label.config(font=new_font)

    # Background color
    new_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    bg_color.set(new_color)
    root.configure(bg=new_color)
    welcome_label.configure(bg=new_color)

# No resize
root.resizable(False, False)

# Initial background color
bg_color = tk.StringVar()
bg_color.set("#e6e6e6")  # First default color
root.configure(bg=bg_color.get())

# The welcome message
welcome_label = tk.Label(root, text="Welcome to the GUI Program!!!", font=("Arial", 16, "bold"), bg=bg_color.get())
welcome_label.pack(pady=20)

# Button that changes font style and background color
change_style_button = tk.Button(root, text="Change Style and Color", command=change_style_and_color)
change_style_button.pack()

root.mainloop()