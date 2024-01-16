import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def count_char():
    # Get the character from the entry field
    char = entry.get()

    # Check for user input
    if len(char) != 1:
        messagebox.showerror("Input Error", "Please enter a single character.")
        return

    try:
        # Open the file and read its contents
        with open("resources\\sentences.txt", "r") as file:
            content = file.read()

        # Count the occurrences of the character
        count = content.count(char)

        # Display the result
        result_label.config(text=f"The character '{char}' occurs {count} times in the file.")

    except FileNotFoundError:
        messagebox.showerror("File Error", "The file 'sentences.txt' was not found.")

# Create and pack widgets
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Count Character", command=count_char)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
