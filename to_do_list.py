#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []

        # Main Frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        # Title
        self.title = tk.Label(self.main_frame, text="To-Do List", font=('Helvetica', 18, 'bold'))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.main_frame, width=50, height=10, font=('Helvetica', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        # Scrollbar for the Listbox
        self.scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Buttons
        self.add_button = tk.Button(self.main_frame, text="Add Task", width=20, command=self.add_task)
        self.add_button.grid(row=2, column=0, pady=5)

        self.update_button = tk.Button(self.main_frame, text="Update Task", width=20, command=self.update_task)
        self.update_button.grid(row=2, column=1, pady=5)

        self.delete_button = tk.Button(self.main_frame, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.grid(row=3, column=0, pady=5)

        self.exit_button = tk.Button(self.main_frame, text="Exit", width=20, command=root.quit)
        self.exit_button.grid(row=3, column=1, pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.update_listbox()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            current_task = self.tasks[selected_task_index]
            new_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("No Selection", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        else:
            messagebox.showwarning("No Selection", "Please select a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

