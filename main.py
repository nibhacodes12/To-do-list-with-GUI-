from tkinter import *
from tkinter import messagebox
import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)''')
    conn.commit()
    conn.close()

# Add a new task to the database
def add_task(task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, 'Pending'))
    conn.commit()
    conn.close()

# Mark task as completed
def complete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET status = ? WHERE id = ?", ('Completed', task_id))
    conn.commit()
    conn.close()

# Delete task from the database
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Retrieve all tasks from the database
def get_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

# Add task from GUI
def add_task_from_gui():
    task = task_entry.get()
    if task:
        add_task(task)
        task_entry.delete(0, END)
        display_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Complete task from GUI
def complete_task_from_gui():
    try:
        task_id = task_listbox.get(ACTIVE).split(':')[0]
        complete_task(task_id)
        display_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

# Delete task from GUI
def delete_task_from_gui():
    try:
        task_id = task_listbox.get(ACTIVE).split(':')[0]
        delete_task(task_id)
        display_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Display tasks in the GUI
def display_tasks():
    tasks = get_tasks()
    task_listbox.delete(0, END)  # Clear the listbox before updating
    for task in tasks:
        task_listbox.insert(END, f"{task[0]}: {task[1]} [{task[2]}]")

# Main GUI setup
def create_gui():
    global task_entry, task_listbox

    root = Tk()
    root.title("To-Do List Manager")

    # Task input area
    Label(root, text="Enter Task:").grid(row=0, column=0)
    task_entry = Entry(root, width=50)
    task_entry.grid(row=0, column=1)

    add_task_btn = Button(root, text="Add Task", command=add_task_from_gui)
    add_task_btn.grid(row=0, column=2)

    # Task list display
    task_listbox = Listbox(root, width=70, height=15)
    task_listbox.grid(row=1, column=0, columnspan=3)

    # Complete task button
    complete_task_btn = Button(root, text="Complete Task", command=complete_task_from_gui)
    complete_task_btn.grid(row=2, column=0)

    # Delete task button
    delete_task_btn = Button(root, text="Delete Task", command=delete_task_from_gui)
    delete_task_btn.grid(row=2, column=1)

    # Run display
    display_tasks()

    root.mainloop()

# Main loop
def main():
    init_db()
    create_gui()

if __name__ == "__main__":
    main()
