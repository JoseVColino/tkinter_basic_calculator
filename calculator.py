import tkinter as tk

def press(key):
    entry_var.set(entry_var.get() + key)

def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

root = tk.Tk()
root.title("Basic Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for b in buttons:
    action = calculate if b == '=' else lambda x=b: press(x)
    tk.Button(root, text=b, padx=20, pady=20, command=action if b == '=' else action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', padx=20, pady=20, command=clear).grid(row=row, column=0, columnspan=4, sticky="we")

root.mainloop()
