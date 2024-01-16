import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("200x250")

# input frame
input_frame = tk.Frame(root, bg='light blue')
input_frame.pack(fill='both', expand=True)

title_label = tk.Label(input_frame, text="Welcome!", fg='blue', bg='light blue')
title_label.pack(pady=10)

name_var = tk.StringVar()
name_entry = tk.Entry(input_frame, textvariable=name_var)
name_entry.pack(pady=10)

color_var = tk.StringVar()
color_dropdown = ttk.Combobox(input_frame, textvariable=color_var)
color_dropdown['values'] = ('Red', 'Green', 'Blue', 'Black')
color_dropdown.pack(pady=10)

# The display frame
display_frame = tk.Frame(root, bg='light green')
display_frame.pack(fill='both', expand=True)

greeting_label = tk.Label(display_frame, text="", bg='light green')
greeting_label.pack(pady=10)

def update_greeting():
    greeting = "Hello, " + name_var.get()
    greeting_label.config(text=greeting, fg=color_var.get())

update_button = tk.Button(input_frame, text="Update Greeting", command=update_greeting)
update_button.pack(pady=10)

root.mainloop()
