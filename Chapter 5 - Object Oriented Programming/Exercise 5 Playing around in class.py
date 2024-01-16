import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Animal class with hello, noise, and details methods
class Animal:
    def __init__(self, type, name, color, age, weight, noise):
        self.type = type  
        self.name = name  
        self.color = color  
        self.age = age  
        self.weight = weight  
        self.noise = noise  

    # Method to say hello
    def sayHello(self):
        return f"Hello, my name is {self.name}."  #hello message

    # Method to make noise
    def makeNoise(self):
        return self.noise  

    # Method to get animal details
    def animalDetails(self):
        return f"I am a {self.color} {self.type}, {self.age} years old, weighing {self.weight} kg."  #details

# Func to show message
def show_message():
    # Getting data for variables
    animal_type = type_entry.get()  
    name = name_entry.get()  
    color = color_entry.get()  
    age = age_entry.get()  
    weight = weight_entry.get()  
    noise = noise_entry.get()  

    animal = Animal(animal_type, name, color, age, weight, noise)  # Animal object
    hello_message = animal.sayHello()  # Get hello message
    noise_message = animal.makeNoise()  # Get noise
    details_message = animal.animalDetails()  # Get details

    messagebox.showinfo("Animal Details", f"{hello_message}\n{noise_message}\n{details_message}")  # Show details

# Labels and entries for type, name, color, age, weight, and noise
type_label = tk.Label(root, text="Type")
type_label.pack()
type_entry = tk.Entry(root)  
type_entry.pack()

name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)  
name_entry.pack()

color_label = tk.Label(root, text="Color")
color_label.pack()
color_entry = tk.Entry(root)  
color_entry.pack()

age_label = tk.Label(root, text="Age")
age_label.pack()
age_entry = tk.Entry(root)  
age_entry.pack()

weight_label = tk.Label(root, text="Weight")
weight_label.pack()
weight_entry = tk.Entry(root)  
weight_entry.pack()

noise_label = tk.Label(root, text="Noise")
noise_label.pack()
noise_entry = tk.Entry(root)  
noise_entry.pack()

# Button to show animal details
button = tk.Button(root, text="Show Animal Details", command=show_message)
button.pack()

root.mainloop()
