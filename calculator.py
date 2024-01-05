import tkinter as tk
from tkinter import ttk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        result_var.set("Invalid input. Please enter valid numbers.")
        return

    choice = operation_var.get()

    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "Division"

    result_var.set(f"{operation} result: {result}")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_num1 = ttk.Label(frame, text="Enter first number:")
label_num1.grid(row=0, column=0, pady=5)

entry_num1 = ttk.Entry(frame)
entry_num1.grid(row=0, column=1, pady=5)

label_num2 = ttk.Label(frame, text="Enter second number:")
label_num2.grid(row=1, column=0, pady=5)

entry_num2 = ttk.Entry(frame)
entry_num2.grid(row=1, column=1, pady=5)

label_operation = ttk.Label(frame, text="Select operation:")
label_operation.grid(row=2, column=0, pady=5)

operation_var = tk.IntVar()
operation_var.set(1)

radio_add = ttk.Radiobutton(frame, text="Addition", variable=operation_var, value=1)
radio_add.grid(row=2, column=1, pady=5, sticky=tk.W)

radio_subtract = ttk.Radiobutton(frame, text="Subtraction", variable=operation_var, value=2)
radio_subtract.grid(row=2, column=1, pady=5, sticky=tk.E)

radio_multiply = ttk.Radiobutton(frame, text="Multiplication", variable=operation_var, value=3)
radio_multiply.grid(row=3, column=1, pady=5, sticky=tk.W)

radio_divide = ttk.Radiobutton(frame, text="Division", variable=operation_var, value=4)
radio_divide.grid(row=3, column=1, pady=5, sticky=tk.E)

button_calculate = ttk.Button(frame, text="Calculate", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_var)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
