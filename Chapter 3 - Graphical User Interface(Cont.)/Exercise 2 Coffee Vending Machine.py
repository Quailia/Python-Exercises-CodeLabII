import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Coffee Vending Machine")

def create_widgets():
    # Coffee Select
    coffee_label = tk.Label(root, text="Select coffee type:")
    coffee_label.pack()
    for coffee, image in coffee_types.items():
        rb = tk.Radiobutton(root, text=coffee, variable=coffee_var, value=coffee, image=image, compound="right")
        rb.pack(side="left")

    # Milk and sugar
    options_label = tk.Label(root, text="Select options:")
    options_label.pack()
    for option, var in option_vars.items():
        cb = tk.Checkbutton(root, text=option, variable=var)
        cb.pack()

    # Enter money
    money_label = tk.Label(root, text="Enter money:")
    money_label.pack()
    money_entry = tk.Entry(root, textvariable=money_var)
    money_entry.pack()

    # Order button
    order_button = tk.Button(root, text="Order", command=order)
    order_button.pack()

def order():
    coffee = coffee_var.get()
    options = [option for option, var in option_vars.items() if var.get()]
    money = money_var.get()

    message = f"You ordered a {coffee} with {', '.join(options)}.\n"
    message += f"You paid {money}."

    messagebox.showinfo("Order", message)

# Coffee images
coffee_types = {
        "Espresso": tk.PhotoImage(file="resources\espresso.png"),
        "Latte": tk.PhotoImage(file="resources\latte.png"),
        "Cappuccino": tk.PhotoImage(file="resources\cappuccino.png")
        }
coffee_var = tk.StringVar()
coffee_var.set(list(coffee_types.keys())[0])

# Coffee Options
options = ["Sugar", "Milk"]
option_vars = {option: tk.BooleanVar() for option in options}

# Money
money_var = tk.DoubleVar()

create_widgets()

root.mainloop()
