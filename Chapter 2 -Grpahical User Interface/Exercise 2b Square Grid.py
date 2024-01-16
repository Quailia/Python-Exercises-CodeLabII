import tkinter as tk

root = tk.Tk()
root.title("GUI Pack Example")

# Frames with a border width of 5
left_frame = tk.Frame(root, borderwidth=5, relief=tk.SUNKEN)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(root, borderwidth=5, relief=tk.SUNKEN)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Labels
label_a = tk.Label(left_frame, text="A",fg= "white", bg="#1B2136", width=20, height=5)
label_a.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label_b = tk.Label(left_frame, text="B", bg="white", width=20, height=5)
label_b.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

label_c = tk.Label(right_frame, text="C", bg="white", width=20, height=5)
label_c.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label_d = tk.Label(right_frame, text="D",fg= "white", bg="#1B2136", width=20, height=5)
label_d.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()
