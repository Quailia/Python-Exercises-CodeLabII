import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")

def login():
    username = entry_username.get()
    password = entry_password.get()

    # allowed username and pw
    if username == "catts" and password == "cattt":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# username part
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="E")

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# pw part
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="E")

entry_password = tk.Entry(root, show="*")  # Entry widget for password, text hidden with '*'
entry_password.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
