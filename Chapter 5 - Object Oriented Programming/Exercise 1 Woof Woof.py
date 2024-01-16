import tkinter as tk

root = tk.Tk()
root.title("Dog Info")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def woof(self):
        return "WWooof!!"


dog1 = Dog("Fido", 5)
dog2 = Dog("Buddy", 7)

# Data output
for i, dog in enumerate([dog1, dog2], start=1):
    tk.Label(root, text=f"Dog {i}:").grid(row=i-1, column=0)
    tk.Label(root, text=f"Name: {dog.name}, Age: {dog.age}").grid(row=i-1, column=1)

# woofin tha oldest dog
# Lambda is a function that can be used in the key here of max, it accesses every age in all the dog classes and returns the biggest one
oldest_dog = max(dog1, dog2, key=lambda dog: dog.age)
woof_text = f"The oldest dog is {oldest_dog.name} and it says: {oldest_dog.woof()}"
tk.Label(root, text=woof_text).grid(row=2, column=0, columnspan=2)

root.mainloop()
