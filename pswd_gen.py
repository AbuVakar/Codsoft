import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        result_var.set("Invalid input. Please enter a valid number.")
        return

    if length <= 0:
        result_var.set("Invalid length. Please enter a positive number.")
        return

    password = generate_password(length)
    result_var.set(f"Generated Password: {password}")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_length = ttk.Label(frame, text="Enter the desired length:")
label_length.grid(row=0, column=0, pady=5)

entry_length = ttk.Entry(frame)
entry_length.grid(row=0, column=1, pady=5)

button_generate = ttk.Button(frame, text="Generate Password", command=generate_and_display_password)
button_generate.grid(row=1, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_var)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
