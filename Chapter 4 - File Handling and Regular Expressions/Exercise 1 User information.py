import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.geometry("200x300")

# Func to write data to file
def write_to_file():
    name = name_entry.get()  # Name from entry
    age = age_entry.get()  # Age from entry
    hometown = hometown_entry.get()  # Hometown from entry

    with open('bio.txt', 'w') as file:  # Open file in write mode
        file.write(f"{name}\n{age}\n{hometown}")  # Write data to file
    
    update_preview()


# Update file preview label
def update_preview():
    if os.path.exists('bio.txt'):  # Check if file exists
        with open('bio.txt', 'r') as file:  # Open file in read mode
            data = file.read()  # Read data from file
        preview_label.config(text=f"File Preview:\n{data}")
    else:
        preview_label.config(text="File Preview:\nNo data available")

# Labels and entries for name, age, and hometown
name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

hometown_label = tk.Label(root, text="Hometown")
hometown_label.pack()
hometown_entry = tk.Entry(root)
hometown_entry.pack()

preview_label = tk.Label(root, text="File Preview:\nNo data available")
preview_label.pack()

# Read button
write_button = tk.Button(root, text="Write to file", command=write_to_file)
write_button.pack()



root.mainloop()
