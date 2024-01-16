import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Student Management System")
root.geometry("350x770")

# Inserting image
img = ImageTk.PhotoImage(Image.open("Resources/campus logo.png"))
imgLabel = tk.Label(root, image=img)
imgLabel.pack()

# White background behind form
back_frame = tk.Frame(root, bg="white")
back_frame.pack(fill="both", expand=True)

# Creating the form
form_frame = tk.Frame(back_frame)  # Place form fields on the background frame
form_frame.place(x=20, y=20, width=310)  # Adjust placement as needed


Name = tk.Label(form_frame, text=" Student Management System", font=("Roboto",16,"bold"), fg="#22263d")
Name.pack()

# Registration lavel
registration_label = tk.Label(form_frame, text="New Student Registration\n", font=("Roboto",12,"bold"), fg="#22263d")
registration_label.pack()

# Labels and entry fields
labels = ["Student Name", "Mobile Number", "Email ID", "Home Address"]
for i, label in enumerate(labels):
    row = tk.Frame(form_frame)
    row.pack(fill="x", pady=5)
    tk.Label(row, text=label, width=20).pack(side="left")
    tk.Entry(row).pack(side="right", expand=True, fill="x")

# Gender
row = tk.Frame(form_frame)
row.pack(fill="x", pady=5)
tk.Label(row, text="Gender", width=20).pack(side="left")
gender = ttk.Combobox(row, values=["Male", "Female"])
gender.pack(side="right", expand=True, fill="x")

# Courses enrolled
tk.Label(form_frame, text="Course Enrolled").pack(anchor="w")
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
course_var = tk.StringVar()
for i, course in enumerate(courses):
    row = tk.Frame(form_frame)
    row.pack(fill="x", pady=2)
    tk.Radiobutton(row, text=course, variable=course_var, value=course).pack(anchor="w")

# Languages known
tk.Label(form_frame, text="Languages Known").pack(anchor="w")
languages = ["English", "Tagalog", "Hindi/Urdu"]
for i, language in enumerate(languages):
    row = tk.Frame(form_frame)
    row.pack(fill="x", pady=2)
    tk.Checkbutton(row, text=language).pack(anchor="w")

# Communication skill scale
row = tk.Frame(form_frame)
row.pack(fill="x", pady=5)
tk.Label(row, text="Rate your English communication skills", width=30).pack(side="top")
tk.Scale(row, from_=0, to=10, orient=tk.HORIZONTAL).pack(side="bottom", expand=True, fill="x")

# Submit and clear buttons
row = tk.Frame(form_frame)
row.pack(fill="x", pady=20)
tk.Button(row, text="Submit", width=15, height=1, bg="#22263d", fg="#FFFFFF", font=("Roboto",10)).pack(side="left", padx=5)
tk.Button(row, text="Clear", width=15, height=1, bg="#22263d", fg="#FFFFFF", font=("Roboto",10)).pack(side="right", padx=5)

root.mainloop()
