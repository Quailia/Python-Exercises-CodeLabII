import tkinter as tk
from tkinter import messagebox
import re

# Initializing attempt counter
attempts = 0

def check_password():
    global attempts
    # Get password from entry field
    pw = entry.get()

    # Password validation criteria
    if (len(pw)<6 or len(pw)>12):
        msg = "Password length should be between 6 and 12"
    elif not re.search("[a-z]", pw):
        msg = "Password should contain at least 1 letter between a and z"
    elif not re.search("[0-9]", pw):
        msg = "Password should contain at least 1 number between 0 and 9"
    elif not re.search("[A-Z]", pw):
        msg = "Password should contain at least 1 letter between A and Z"
    elif not re.search("[$#@]", pw):
        msg = "Password should contain at least 1 character from $, #, @"
    else:
        msg = "Password is valid"
        attempts = 0  #reset if password is valid

    # Increment counter
    attempts += 1

    # Check if maximum attempts reached
    if attempts > 5:
        msg = "Maximum attempts reached. Authorities have been alerted!"
        attempts = 0 
    elif attempts <= 5 and msg != "Password is valid":
        msg += f". You have {5 - attempts} attempts remaining."

    # Display result
    result_label.config(text=msg)

# Create thew main window
root = tk.Tk()

# Create widgets
entry = tk.Entry(root)
button = tk.Button(root, text="Check Password", command=check_password)
result_label = tk.Label(root, text="")

# Place widgets in the window
entry.pack()
button.pack()
result_label.pack()

root.mainloop()