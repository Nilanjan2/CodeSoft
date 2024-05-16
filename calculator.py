#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Labels and Entry boxes for numbers
        self.label1 = tk.Label(root, text="Enter first number:")
        self.label1.grid(row=0, column=0, padx=10, pady=5)

        self.entry1 = tk.Entry(root, width=20)
        self.entry1.grid(row=0, column=1, padx=10, pady=5)

        self.label2 = tk.Label(root, text="Enter second number:")
        self.label2.grid(row=1, column=0, padx=10, pady=5)

        self.entry2 = tk.Entry(root, width=20)
        self.entry2.grid(row=1, column=1, padx=10, pady=5)

        # Dropdown menu for operation choice
        self.label3 = tk.Label(root, text="Choose an operation:")
        self.label3.grid(row=2, column=0, padx=10, pady=5)

        self.operation_var = tk.StringVar(root)
        self.operation_var.set("Select")
        self.operations = ["Add", "Subtract", "Multiply", "Divide"]
        self.operation_menu = tk.OptionMenu(root, self.operation_var, *self.operations)
        self.operation_menu.grid(row=2, column=1, padx=10, pady=5)

        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result display
        self.result_label = tk.Label(root, text="Result: ", font=('Helvetica', 14))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            operation = self.operation_var.get()

            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Please select a valid operation")
                return

            self.result_label.config(text=f"Result: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

