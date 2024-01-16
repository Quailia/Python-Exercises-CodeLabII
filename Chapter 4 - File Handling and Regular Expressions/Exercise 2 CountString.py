import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()

# Function to count occurrences for each predefined string
def count_occurrence_for_string(string_to_search):
    count = 0  #Initializing count

    if os.path.exists("resources\\sentences.txt"):
        with open("resources\\sentences.txt", "r") as file:
            data = file.read()
            count = data.lower().count(string_to_search.lower())  # Counting for the specific string in a case-insensitive way

        # Displaying count below the button
        result_label.config(text=f"'{string_to_search}': {count}")

# Defining function to count custom string
def count_custom_string():
    string_to_search = search_entry.get()  # Getting string from entry field
    count = 0 

    if os.path.exists("resources\\sentences.txt"):
        with open("resources\\sentences.txt", "r") as file:
            data = file.read()
            count = data.lower().count(string_to_search.lower())  # Counting but for custom string in a case-insensitive way

        # Displaying count below the buttons
        result_label.config(text=f"'{string_to_search}': {count}")

# Labels, entries and buttons
search_label = tk.Label(root, text="Search")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

# Create buttons for each predefined string
for string_to_search in ["Hello my name is Peter Parker", "I love Python Programming", "Love", "Enemy"]:
    button = tk.Button(root, text=string_to_search, command=lambda s=string_to_search: count_occurrence_for_string(s))
    button.pack()

count_custom_string_button = tk.Button(root, text="Count custom string", command=count_custom_string)
count_custom_string_button.pack()

# Displaying results bewlow the buttons
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
