import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip   # pip install pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length!")
        return

    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4.")
        return

    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_numbers.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Please select at least one character set!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

# Main window
root = tk.Tk()
root.title("Neon Password Generator")
root.geometry("450x350")
root.config(bg="#0d0d0d")

# Neon style colors
neon_blue = "#00f5ff"
neon_green = "#39ff14"
neon_pink = "#ff1493"

# Title
title_label = tk.Label(root, text="⚡ Neon Password Generator ⚡", 
                       fg=neon_blue, bg="#0d0d0d", font=("Consolas", 16, "bold"))
title_label.pack(pady=15)

# Password length input
tk.Label(root, text="Password Length:", fg=neon_green, bg="#0d0d0d", font=("Consolas", 12)).pack(pady=5)
length_entry = tk.Entry(root, width=10, font=("Consolas", 12), bg="#1a1a1a", fg="white", insertbackground="white")
length_entry.pack()

# Checkboxes (force ticks to be visible with selectcolor)
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper, bg="#0d0d0d", 
               fg=neon_pink, selectcolor="#0d0d0d", activeforeground=neon_pink).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower, bg="#0d0d0d", 
               fg=neon_pink, selectcolor="#0d0d0d", activeforeground=neon_pink).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg="#0d0d0d", 
               fg=neon_pink, selectcolor="#0d0d0d", activeforeground=neon_pink).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, bg="#0d0d0d", 
               fg=neon_pink, selectcolor="#0d0d0d", activeforeground=neon_pink).pack(anchor="w", padx=50)

# Generate button
tk.Button(root, text="⚡ Generate", command=generate_password, 
          bg=neon_blue, fg="black", font=("Consolas", 12, "bold")).pack(pady=12)

# Result box
result_entry = tk.Entry(root, width=30, font=("Consolas", 14), 
                        bg="#1a1a1a", fg=neon_green, insertbackground="white", justify="center")
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="📋 Copy", command=copy_to_clipboard, 
          bg=neon_green, fg="black", font=("Consolas", 12, "bold")).pack(pady=10)

root.mainloop()
