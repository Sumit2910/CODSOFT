import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
        tasks.pop(selected_task_index[0])
    else:
        messagebox.showwarning("Warning", "You must select a task.")

app = tk.Tk()
app.title("To-Do List")

task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=10)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)

app.mainloop()
