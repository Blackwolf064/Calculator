import tkinter as tk
from tkinter import messagebox
import math
# root = tk.Tk()

# Function to add text to the entry widget
def add_to_expression(symbol):
    if symbol == "sqrt":
        # Automatically add the square root with parentheses around the input
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.sqrt({current})")
    elif symbol == "^":
        entry.insert(tk.END, "**")  # Python uses '**' for exponentiation
    else:
        entry.insert(tk.END, symbol)

# Function to evaluate the expression entered
def evaluate_expression():
    try:
        # Evaluate the expression in the entry widget
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete the last character
def delete_last():
    current = entry.get()
    if current:  # Check if there’s any text to delete
        entry.delete(len(current) - 1, tk.END)

# Create the main window
root = tk.Tk()
root.title("Kate's Calculator")
root.configure(bg="#ADD8E6")

# Create an entry widget for displaying expressions
entry = tk.Entry(root, width=30, font=("Comic Sans MS", 18), borderwidth=2, relief="solid", justify="right", bg="#FFFFFF")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=15)

# Define button labels and their grid positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("^", 4, 1), ("sqrt", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("=", 5, 1), ("DEL", 5, 2), ("%", 5, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=10, height=2, command=evaluate_expression).grid(row=row, column=col)
    elif text == "C":
        tk.Button(root, text=text, width=10, height=2, command=clear_entry).grid(row=row, column=col, padx=5, pady=5)
    elif text == "DEL":
        tk.Button(root, text=text, width=10, height=2, command=delete_last).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=10, height=2, command=lambda t=text: add_to_expression(t)).grid(row=row, column=col, padx=5, pady=5)

# Run the main event loop
root.mainloop()

