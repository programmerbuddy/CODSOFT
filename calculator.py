import tkinter as tk
from tkinter import messagebox
import json
import os

TODO_FILE = "todo_list_gui.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task_description = entry_task.get()
    if task_description:
        tasks.append({"task": task_description, "done": False})
        save_tasks(tasks)
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty.")

def mark_task_done():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

def delete_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "[Done]" if task["done"] else "[Pending]"
        listbox_tasks.insert(tk.END, f"{task['task']} {status}")

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox_tasks = tk.Listbox(frame, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=52)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack(pady=5)

button_mark_done = tk.Button(root, text="Mark Task as Done", width=48, command=mark_task_done)
button_mark_done.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack(pady=5)

update_task_list()

root.mainloop()
