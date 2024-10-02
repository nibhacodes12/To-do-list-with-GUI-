
---

# To-Do List Manager

The **To-Do List Manager** is a simple desktop application built using Python and Tkinter. It allows users to create, manage, and track their daily tasks. Users can add tasks, mark tasks as completed, delete tasks, and view all tasks in one place. The data is stored in an SQLite database to ensure persistence across sessions.

## Features

- **Add Tasks**: Input a task description to add it to the to-do list.
- **Mark as Completed**: Mark tasks as completed from the list.
- **Delete Tasks**: Remove tasks from the list.
- **View All Tasks**: Display all tasks, including pending and completed tasks.
- **Persistent Storage**: Tasks are stored in an SQLite database for future access.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: Used for creating the graphical user interface.
- **SQLite**: Database used for storing tasks.

## Requirements

- Python 3.x
- Tkinter (usually pre-installed with Python)
- SQLite (comes with Python)

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/todo-list-manager.git
   ```

2. Navigate to the project directory:
   ```bash
   cd todo-list-manager
   ```

3. Run the program:
   ```bash
   python todo_list.py
   ```

## How to Use

1. **Add a Task**:
   - Type the task description into the input field and click "Add Task".
   - The task will appear in the list with the status "Pending".

2. **Mark Task as Completed**:
   - Select a task from the list and click the "Complete Task" button to mark it as completed.

3. **Delete a Task**:
   - Select a task from the list and click the "Delete Task" button to remove it from the list.

## License

This project is licensed under the MIT License.

---
