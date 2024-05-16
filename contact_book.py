#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = self.load_contacts()
        
        # Main Frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)
        
        # Title
        self.title = tk.Label(self.main_frame, text="Contact Book", font=('Helvetica', 18, 'bold'))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Buttons
        self.add_button = tk.Button(self.main_frame, text="Add Contact", width=20, command=self.add_contact)
        self.add_button.grid(row=1, column=0, padx=10, pady=5)
        
        self.view_button = tk.Button(self.main_frame, text="View Contacts", width=20, command=self.view_contacts)
        self.view_button.grid(row=1, column=1, padx=10, pady=5)
        
        self.search_button = tk.Button(self.main_frame, text="Search Contact", width=20, command=self.search_contact)
        self.search_button.grid(row=2, column=0, padx=10, pady=5)
        
        self.update_button = tk.Button(self.main_frame, text="Update Contact", width=20, command=self.update_contact)
        self.update_button.grid(row=2, column=1, padx=10, pady=5)
        
        self.delete_button = tk.Button(self.main_frame, text="Delete Contact", width=20, command=self.delete_contact)
        self.delete_button.grid(row=3, column=0, padx=10, pady=5)
        
        self.exit_button = tk.Button(self.main_frame, text="Exit", width=20, command=root.quit)
        self.exit_button.grid(row=3, column=1, padx=10, pady=5)
        
    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")
        
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        self.save_contacts()
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        contacts_window = tk.Toplevel(self.root)
        contacts_window.title("View Contacts")
        
        tk.Label(contacts_window, text="Name", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(contacts_window, text="Phone Number", font=('Helvetica', 12, 'bold')).grid(row=0, column=1, padx=10, pady=5)
        
        for idx, contact in enumerate(self.contacts, start=1):
            tk.Label(contacts_window, text=contact["name"]).grid(row=idx, column=0, padx=10, pady=5)
            tk.Label(contacts_window, text=contact["phone"]).grid(row=idx, column=1, padx=10, pady=5)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not search_term:
            return
        results = [contact for contact in self.contacts if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]]
        
        if not results:
            messagebox.showinfo("No Results", "No contacts found.")
            return
        
        results_window = tk.Toplevel(self.root)
        results_window.title("Search Results")
        
        tk.Label(results_window, text="Name", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(results_window, text="Phone Number", font=('Helvetica', 12, 'bold')).grid(row=0, column=1, padx=10, pady=5)
        
        for idx, contact in enumerate(results, start=1):
            tk.Label(results_window, text=contact["name"]).grid(row=idx, column=0, padx=10, pady=5)
            tk.Label(results_window, text=contact["phone"]).grid(row=idx, column=1, padx=10, pady=5)

    def update_contact(self):
        name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        if not name:
            return
        contact = next((contact for contact in self.contacts if contact["name"].lower() == name.lower()), None)
        if not contact:
            messagebox.showinfo("Error", "Contact not found.")
            return
        
        phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=contact["phone"])
        email = simpledialog.askstring("Input", "Enter new email:", initialvalue=contact["email"])
        address = simpledialog.askstring("Input", "Enter new address:", initialvalue=contact["address"])
        
        contact["phone"] = phone
        contact["email"] = email
        contact["address"] = address
        
        self.save_contacts()
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        if not name:
            return
        self.contacts = [contact for contact in self.contacts if contact["name"].lower() != name.lower()]
        self.save_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully.")

def main():
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()

if __name__ == "__main__":
    main()

