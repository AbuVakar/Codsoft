import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Title Label with Color
        title_label = tk.Label(master, text="To-Do List App", font=("Helvetica", 16), fg="orange")
        title_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.tasks = []
        self.load_tasks()

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=40)
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Add Task Button with Color
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Remove Task Button with Color
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, bg="#FF5733", fg="white")
        self.remove_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        # Update Task Button with Color
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#4285F4", fg="white")
        self.update_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        # Task Listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

        self.populate_listbox()

    def load_tasks(self):
        try:
            with open("todolist_tkinter.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("todolist_tkinter.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def populate_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

    def add_task(self):
        new_task = self.task_var.get()
        if new_task:
            self.tasks.append(new_task)
            self.save_tasks()
            self.populate_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            self.populate_listbox()
            messagebox.showinfo("Task Removed", f"Task removed: {removed_task}")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            updated_task = self.task_var.get()
            if updated_task:
                self.tasks[index] = updated_task
                self.save_tasks()
                self.populate_listbox()
                self.task_var.set("")
                messagebox.showinfo("Task Updated", "Task updated successfully.")
            else:
                messagebox.showwarning("Warning", "Task description cannot be empty.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
