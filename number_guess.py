import tkinter as tk
import random

number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            feedback.set("Too low!")
        elif guess > number:
            feedback.set("Too high!")
        else:
            feedback.set("Correct!")
        
        atempts.set(atempts.get() + 1)
        formatted_text.set(f'Atempts: {atempts.get()}')

    except ValueError:
        feedback.set("Enter a valid number.")

root = tk.Tk()
root.title("Guess the Number")

tk.Label(root, text="You have 8 atempts to guess the number!\n").pack()
tk.Label(root, text="Guess a number (1-100):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check_guess).pack()

feedback = tk.StringVar()
atempts = tk.IntVar()
atempts.set(0)
formatted_text = tk.StringVar()
formatted_text.set(f'Atempts: {atempts.get()}')

tk.Label(root, textvariable=feedback).pack()

tk.Label(root, textvariable=formatted_text).pack()


root.mainloop()