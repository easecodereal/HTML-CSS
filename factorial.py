import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    try:
        num = int(entry.get())  # Get the number from the entry widget
        if num < 0:
            messagebox.showerror("Error", "Please enter a non-negative integer.")
            return
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        result_label.config(text=f"The factorial of {num} is: {factorial}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
window = tk.Tk()
window.title("Factorial Calculator")

# Create and place widgets
label = tk.Label(window, text="Enter a number:")
label.pack()

entry = tk.Entry(window)
entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_factorial)
calculate_button.pack()

result_label = tk.Label(window, text="", fg="green")
result_label.pack()

# Run the main event loop
window.mainloop()
