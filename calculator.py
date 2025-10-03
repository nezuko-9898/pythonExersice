import tkinter as tk

def calculate(op):
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        if op == "+":
            result.set(x + y)
        elif op == "-":
            result.set(x - y)
        elif op == "*":
            result.set(x * y)
        elif op == "/":
            result.set("Error" if y == 0 else x / y)
    except ValueError:
        result.set("Invalid input")

# Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Result
result = tk.StringVar()
tk.Label(root, text="Result:").pack()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

for op in ["+", "-", "*", "/"]:
    tk.Button(btn_frame, text=op, width=5, command=lambda o=op: calculate(o)).pack(side="left", padx=5)

# Run the app
root.mainloop()
