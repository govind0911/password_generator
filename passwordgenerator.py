import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip

root = tk.Tk()
root.title("Neon Password Generator")
root.geometry("550x500")
root.configure(bg="#0d0d0d")
root.resizable(False, False)

neon_blue = "#00f5ff"
neon_green = "#39ff14"
neon_pink = "#ff1493"
dark_bg = "#0d0d0d"
box_bg = "#1a1a1a"

def calculate_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def generate_password(event=None):
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length.")
        return

    selected_sets = []

    if var_upper.get():
        selected_sets.append(string.ascii_uppercase)

    if var_lower.get():
        selected_sets.append(string.ascii_lowercase)

    if var_numbers.get():
        selected_sets.append(string.digits)

    if var_symbols.get():
        selected_sets.append(string.punctuation)

    if not selected_sets:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    if length < len(selected_sets):
        messagebox.showerror(
            "Error",
            f"Length must be at least {len(selected_sets)}."
        )
        return

    password_chars = [
        secrets.choice(charset)
        for charset in selected_sets
    ]

    all_chars = "".join(selected_sets)

    password_chars.extend(
        secrets.choice(all_chars)
        for _ in range(length - len(password_chars))
    )

    secrets.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)

    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

    if not show_password_var.get():
        result_entry.config(show="•")
    else:
        result_entry.config(show="")

    strength_var.set(
        f"Strength: {calculate_strength(password)}"
    )

    if auto_copy_var.get():
        pyperclip.copy(password)

def copy_password():
    password = result_entry.get()

    if not password:
        messagebox.showerror("Error", "No password generated.")
        return

    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

def clear_password():
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    strength_var.set("Strength: N/A")

def toggle_password():
    if show_password_var.get():
        result_entry.config(show="")
    else:
        result_entry.config(show="•")

title = tk.Label(
    root,
    text="⚡ Neon Password Generator ⚡",
    bg=dark_bg,
    fg=neon_blue,
    font=("Consolas", 18, "bold")
)
title.pack(pady=15)

length_frame = tk.Frame(root, bg=dark_bg)
length_frame.pack(pady=10)

tk.Label(
    length_frame,
    text="Password Length",
    bg=dark_bg,
    fg=neon_green,
    font=("Consolas", 12)
).pack()

length_entry = tk.Entry(
    length_frame,
    width=12,
    justify="center",
    font=("Consolas", 13),
    bg=box_bg,
    fg="white",
    insertbackground="white"
)
length_entry.insert(0, "16")
length_entry.pack(pady=5)

options_frame = tk.Frame(root, bg=dark_bg)
options_frame.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
show_password_var = tk.BooleanVar(value=False)
auto_copy_var = tk.BooleanVar(value=False)

checkboxes = [
    ("Uppercase Letters", var_upper),
    ("Lowercase Letters", var_lower),
    ("Numbers", var_numbers),
    ("Symbols", var_symbols),
    ("Show Password", show_password_var),
    ("Auto Copy", auto_copy_var)
]

for text, variable in checkboxes:
    tk.Checkbutton(
        options_frame,
        text=text,
        variable=variable,
        bg=dark_bg,
        fg=neon_pink,
        activeforeground=neon_pink,
        activebackground=dark_bg,
        selectcolor=dark_bg,
        command=toggle_password if text == "Show Password" else None,
        font=("Consolas", 11)
    ).pack(anchor="w")

button_frame = tk.Frame(root, bg=dark_bg)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="⚡ Generate",
    command=generate_password,
    bg=neon_blue,
    fg="black",
    font=("Consolas", 12, "bold"),
    width=12
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="📋 Copy",
    command=copy_password,
    bg=neon_green,
    fg="black",
    font=("Consolas", 12, "bold"),
    width=12
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="🗑 Clear",
    command=clear_password,
    bg=neon_pink,
    fg="black",
    font=("Consolas", 12, "bold"),
    width=12
).grid(row=0, column=2, padx=5)

result_entry = tk.Entry(
    root,
    width=40,
    justify="center",
    font=("Consolas", 15),
    bg=box_bg,
    fg=neon_green,
    insertbackground="white",
    show="•"
)
result_entry.pack(pady=15)

strength_var = tk.StringVar(value="Strength: N/A")

strength_label = tk.Label(
    root,
    textvariable=strength_var,
    bg=dark_bg,
    fg=neon_blue,
    font=("Consolas", 12, "bold")
)
strength_label.pack(pady=5)

footer = tk.Label(
    root,
    text="Secure Password Generator",
    bg=dark_bg,
    fg="#666666",
    font=("Consolas", 10)
)
footer.pack(side="bottom", pady=10)

root.bind("<Return>", generate_password)

root.mainloop()
