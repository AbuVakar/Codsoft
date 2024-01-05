import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.root = tk.Tk()
        self.root.title("Contact Book")

        self.create_widgets()

    def create_widgets(self):
        self.label_name = ttk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

        self.entry_name = ttk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = ttk.Label(self.root, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

        self.entry_phone = ttk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = ttk.Label(self.root, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

        self.entry_email = ttk.Entry(self.root)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = ttk.Label(self.root, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)

        self.entry_address = ttk.Entry(self.root)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.button_add_contact = ttk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.button_add_contact.grid(row=4, column=0, columnspan=2, pady=10)

        self.tree_contacts = ttk.Treeview(self.root, columns=("ID", "Name", "Phone"))
        self.tree_contacts.heading("#0", text="ID")
        self.tree_contacts.heading("ID", text="ID")
        self.tree_contacts.heading("Name", text="Name")
        self.tree_contacts.heading("Phone", text="Phone")
        self.tree_contacts.column("#0", stretch=tk.NO, width=0)  # Hide the ID column
        self.tree_contacts.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.button_search = ttk.Button(self.root, text="Search", command=self.search_contact)
        self.button_search.grid(row=6, column=0, columnspan=2, pady=5)

        self.button_update = ttk.Button(self.root, text="Update", command=self.update_contact)
        self.button_update.grid(row=7, column=0, columnspan=2, pady=5)

        self.button_delete = ttk.Button(self.root, text="Delete", command=self.delete_contact)
        self.button_delete.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.display_contacts()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Incomplete Information", "Name and Phone are required.")

    def display_contacts(self):
        self.tree_contacts.delete(*self.tree_contacts.get_children())
        for idx, contact in enumerate(self.contacts, start=1):
            self.tree_contacts.insert("", "end", values=(idx, contact["Name"], contact["Phone"]))

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts
                              if search_term.lower() in contact["Name"].lower() or
                              search_term in contact["Phone"]]
            if found_contacts:
                self.display_search_results(found_contacts)
            else:
                messagebox.showinfo("Search Result", "No contacts found.")

    def display_search_results(self, results):
        self.tree_contacts.delete(*self.tree_contacts.get_children())
        for idx, contact in enumerate(results, start=1):
            self.tree_contacts.insert("", "end", values=(idx, contact["Name"], contact["Phone"]))

    def update_contact(self):
        selected_item = self.tree_contacts.selection()
        if selected_item:
            contact_idx = int(self.tree_contacts.item(selected_item, "values")[0]) - 1
            contact = self.contacts[contact_idx]

            name = self.entry_name.get()
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()

            if name and phone:
                contact["Name"] = name
                contact["Phone"] = phone
                contact["Email"] = email
                contact["Address"] = address

                self.display_contacts()
                self.clear_entry_fields()
            else:
                messagebox.showwarning("Incomplete Information", "Name and Phone are required.")
        else:
            messagebox.showwarning("No Contact Selected", "Please select a contact to update.")

    def delete_contact(self):
        selected_item = self.tree_contacts.selection()
        if selected_item:
            contact_idx = int(self.tree_contacts.item(selected_item, "values")[0]) - 1
            del self.contacts[contact_idx]
            self.display_contacts()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("No Contact Selected", "Please select a contact to delete.")

    def clear_entry_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
