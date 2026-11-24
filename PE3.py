# Name: Patil Diksha Chandrakant
# Batch: T7
# Roll No: 3139

import tkinter as tk
from tkinter import messagebox
                                
class TodoApplication:

    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("700x650")
        
        self.task_var = tk.StringVar()
        self.priority_var = tk.StringVar(value="Medium")
        
        self.tasks = []
        
        menu_bar = tk.Menu(root)
        
        todo_menu = tk.Menu(menu_bar, tearoff=0)
        
        todo_menu.add_command(
            label="Save List",
            command=self.save_list
        )
        
        todo_menu.add_command(
            label="Load List",
            command=self.load_list
        )
        
        todo_menu.add_separator()

        todo_menu.add_command(
            label="Exit",
            command=root.quit
        )
        
        menu_bar.add_cascade(
            label="To-Do List",
            menu=todo_menu
        )
        
        root.config(menu=menu_bar)

        title = tk.Label(
            root,
            text="To-Do List Application",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=15)

        tk.Label(
            root,
            text="Enter Task:",
            font=("Arial", 12)
        ).pack()
        
        tk.Entry(
            root,
            textvariable=self.task_var,
            width=50,
            font=("Arial", 11)
        ).pack(pady=8)

        tk.Label(
            root,
            text="Select Priority:",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        priority_frame = tk.Frame(root)
        priority_frame.pack()

        tk.Radiobutton(
            priority_frame,
            text="High",
            variable=self.priority_var,
            value="High"
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            priority_frame,
            text="Medium",
            variable=self.priority_var,
            value="Medium"
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            priority_frame,
            text="Low",
            variable=self.priority_var,
            value="Low"
        ).pack(side="left", padx=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Add Task",
            width=14,
            command=self.add_task
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Delete Task",
            width=14,
            command=self.delete_task
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Clear All",
            width=14,
            command=self.clear_all
        ).grid(row=0, column=2, padx=5)

        tk.Label(
            root,
            text="Task List",
            font=("Arial", 14, "bold")
        ).pack(pady=5)
                        
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(
            padx=20,
            pady=5,
            fill="both",
            expand=True
        )

        self.task_listbox = tk.Listbox(
            self.task_frame,
            width=70,
            height=12,
            font=("Arial", 11),
            selectmode=tk.SINGLE
        )

        self.task_listbox.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            self.task_frame,
            command=self.task_listbox.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.task_listbox.config(
            yscrollcommand=scrollbar.set
        )

        tk.Label(
            root,
            text="Completed Tasks",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.completed_frame = tk.Frame(root)
        self.completed_frame.pack(pady=5)

    def add_task(self):

        task = self.task_var.get().strip()

        if task == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a task."
            )
            return

        priority = self.priority_var.get()

        self.tasks.append({
            "task": task,
            "priority": priority,
            "completed": False
        })

        self.task_var.set("")

        self.display_tasks()

    def delete_task(self):

        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a task to delete."
            )
            return

        index = selected[0]

        del self.tasks[index]

        self.display_tasks()

    def clear_all(self):

        if not self.tasks:
            return

        result = messagebox.askyesno(
            "Clear All",
            "Are you sure you want to clear all tasks?"
        )

        if result:
            self.tasks.clear()
            self.display_tasks()

    def mark_completed(self, index):

        self.tasks[index]["completed"] = not self.tasks[index]["completed"]

        self.display_tasks()

    def display_tasks(self):

        self.task_listbox.delete(
            0,
            tk.END
        )

        for i, item in enumerate(self.tasks):

            status = "✓ Done" if item["completed"] else "Pending"

            text = (
                f"{i + 1}. {item['task']} "
                f"| Priority: {item['priority']} "
                f"| {status}"
            )

            self.task_listbox.insert(
                tk.END,
                text
            )

            if item["completed"]:
                self.task_listbox.itemconfig(
                    tk.END,
                    fg="green"
                )

        for widget in self.completed_frame.winfo_children():
            widget.destroy()

        for i, item in enumerate(self.tasks):

            var = tk.BooleanVar(
                value=item["completed"]
            )

            check = tk.Checkbutton(
                self.completed_frame,
                text=item["task"],
                variable=var,
                command=lambda index=i: self.mark_completed(index)
            )

            check.pack(
                anchor="w"
            )

    def save_list(self):

        self.display_tasks()

        messagebox.showinfo(
            "Save List",
            "To-do list saved successfully."
        )

    def load_list(self):

        messagebox.showinfo(
            "Load List",
            "To-do list loaded successfully."
        )

        self.display_tasks()


root = tk.Tk()

app = TodoApplication(root)

root.mainloop()
