import tkinter as tk


root = tk.Tk()
root.geometry("160x66")

# Frames
frame_a = tk.Frame(root)
frame_a.pack(side="top", fill="x", expand=True)

frame_cd = tk.Frame(root)
frame_cd.pack(side="top", fill="x")

frame_b = tk.Frame(root)
frame_b.pack(side="top", fill="x")

# Labels
label_a = tk.Label(frame_a, text="A", bg="red", fg="black", width=11, height=1, relief="groove", bd=5)
label_a.pack(side="top", fill="x")

label_d = tk.Label(frame_cd, text="D", bg="white", fg="black", width=11, height=1, relief="flat", bd=1)
label_d.pack(anchor= "e", side="right", fill="none")

label_c = tk.Label(frame_cd, text="C", bg="blue", fg="black", width=11, height=1, relief="flat", bd=1)
label_c.pack(anchor= "s", side= "left", fill="none")

label_b = tk.Label(frame_b, text="B", bg="yellow", fg="black", width=11, height=1, relief="raised", bd=2)
label_b.pack(anchor= "s", side="bottom", fill="none")

# Update position of C and D rel to B
def update_position(Configure):
    b_geometry = label_b.winfo_geometry()
    b_x, b_y = map(int, b_geometry.split('+')[1:3])
    label_c.place(x=b_x - 40, y=b_y)

# Positions update with window resize
root.bind("<Configure>", update_position)

root.mainloop()
