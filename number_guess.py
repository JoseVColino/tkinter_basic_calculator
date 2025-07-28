import tkinter as tk
from tkinter import messagebox
import random

MAX_ATEMPTS = 8
number = random.randint(1, 100)

def check_guess():
    if atempts.get() >= MAX_ATEMPTS:

        messagebox.showinfo("Game Over", f"You've reached the max attempts! The number was {number}.")
        entry.config(state='disabled')
        check_button.config(state='disabled')

        return

    try:
        guess = int(entry.get())

        if guess == last_attempt.get():
            feedback.set("Try to guess a different number!")
            return
        
        last_attempt.set(guess)
        if guess < number:
            feedback.set("the number is higher!")
        elif guess > number:
            feedback.set("the number is lower!")
        else:
            messagebox.showinfo("You Got It!", f"You've guessed the number correctly! It was {number}!")
            entry.config(state='disabled')
            check_button.config(state='disabled')
        
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

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack()

feedback = tk.StringVar()
atempts = tk.IntVar()
last_attempt = tk.IntVar()

atempts.set(0)
formatted_text = tk.StringVar()
formatted_text.set(f'Atempts: {atempts.get()}')

tk.Label(root, textvariable=feedback).pack()
tk.Label(root, textvariable=formatted_text).pack()

print(number)
root.mainloop()