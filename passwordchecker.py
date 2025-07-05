import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Check
    if re.search(r'[A-Z]', password):
        strength_points += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase Check
    if re.search(r'[a-z]', password):
        strength_points += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Digit Check
    if re.search(r'\d', password):
        strength_points += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special Character Check
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|<,./<>?]', password):
        strength_points += 1
    else:
        feedback.append("Add at least one special character (e.g. @, #, !).")

    # Evaluate Strength
    if strength_points == 5:
        return "Strong password 💪", "green"
    elif strength_points >= 3:
        return "Moderate password 🧐", "orange"
    else:
        return "Weak password ⚠️\n" + "\n".join(feedback), "red"

def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Required", "Please enter a password.")
        return

    result, color = check_password_strength(password)
    result_label.config(text=result, fg=color)

# GUI Setup
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x300")
window.config(padx=20, pady=20)

title = tk.Label(window, text="🔐 Password Strength Checker", font=("Arial", 16))
title.pack(pady=10)

entry_label = tk.Label(window, text="Enter your password:")
entry_label.pack()

entry = tk.Entry(window, width=30, show='*')
entry.pack(pady=5)

check_btn = tk.Button(window, text="Check Strength", command=on_check)
check_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
