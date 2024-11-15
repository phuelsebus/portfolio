import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    selected_tasks = listbox_tasks.curselection()
    for index in selected_tasks[::-1]:
        listbox_tasks.delete(index)

window = tk.Tk()
window.title("To-Do List")

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, selectmode=tk.MULTIPLE)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(window, width=50)
entry_task.pack()
entry_task.bind("<Return>", add_task)

button_delete_task = tk.Button(window, text="Delete selected tasks", width=48, command=delete_task)
button_delete_task.pack()
def toggle_task(event):
    widget = event.widget
    index = widget.curselection()[0]
    widget.delete(index)


window.mainloop()
