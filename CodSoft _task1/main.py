import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo List App")
        self.geometry("500x500")
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="gray")

        self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry")
        self.task_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.task_input.insert(0, "Enter your todo here...")
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        self.add_button = ttk.Button(self, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.done_button = ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done)
        self.done_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.delete_button = ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        self.stats_button = ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_stats)
        self.stats_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.load_tasks()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
    
    def view_stats(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task = self.task_input.get()
        if task != "Enter your todo here...":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()
    
    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()
    
    def clear_placeholder(self, event):
        if self.task_input.get() == "Enter your todo here...":
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.task_input.get() == "":
            self.task_input.insert(0, "Enter your todo here...")
            self.task_input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()
