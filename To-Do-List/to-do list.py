import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASK_FILE = "To-Do-List\list.txt"

# List to store tasks and their check states
tasks = []
task_vars = []  # List to store BooleanVar objects

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                # Split task and state or set default state
                parts = line.split("|")
                task = parts[0]
                state = parts[1] if len(parts) > 1 else "False"  # Default to unchecked
                tasks.append(task)
                task_vars.append(tk.BooleanVar(value=state == "True"))  # Load state
        update_task_list()

# Function to save tasks to the file
def save_tasks():
    with open(TASK_FILE, "w") as file:
        for i, task in enumerate(tasks):
            # Save task and its checkbox state
            file.write(f"{task}|{task_vars[i].get()}\n")

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_vars.append(tk.BooleanVar(value=False))  # Add unselected checkbox
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Function to update the task list in the GUI with Checkbuttons
def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        # Create a frame for each task
        task_item_frame = tk.Frame(task_frame, bg="#2E2E2E")
        task_item_frame.pack(fill="x", pady=2)

        # Checkbox for marking task completion
        checkbox = tk.Checkbutton(
            task_item_frame, text=task, variable=task_vars[i],
            fg="white", bg="#2E2E2E", selectcolor="#2E2E2E",
            activebackground="#2E2E2E", anchor="w",
            font=("Arial", 10)
        )
        checkbox.pack(side="left", fill="x", expand=True)

# Function to remove a task
def remove_task():
    global tasks, task_vars
    new_tasks = []
    new_task_vars = []

    for task, var in zip(tasks, task_vars):
        if not var.get():  # Keep tasks that are not selected
            new_tasks.append(task)
            new_task_vars.append(var)

    tasks = new_tasks
    task_vars = new_task_vars
    update_task_list()

# Function to exit the app
def exit_app():
    save_tasks()  # Save the tasks with their checkbox state
    app.quit()

# GUI Setup
app = tk.Tk()
app.title("To-Do List")

# Make the window always on top
app.wm_attributes("-topmost", True)

# Remove the default title bar
app.overrideredirect(True)

# Allow the user to drag the window
def move_window(event):
    app.geometry(f"+{event.x_root}+{event.y_root}")

app.bind("<B1-Motion>", move_window)

# Apply Dark Theme for Main Content
app.configure(bg="#1E1E1E", bd=1,)

# Make the window transparent when it loses focus
def on_focus_out(event):
    app.wm_attributes("-alpha", 0.5)  # Make the window semi-transparent

def on_focus_in(event):
    app.wm_attributes("-alpha", 1.0)  # Restore full opacity

# Bind focus events
app.bind("<FocusOut>", on_focus_out)
app.bind("<FocusIn>", on_focus_in)

# Task List Display
task_frame = tk.Frame(app, bg="#2E2E2E")
task_frame.pack(padx=0, pady=0, fill="both", expand=True)

# Input Field
task_entry = tk.Entry(
    app, width=38, bg="#2E2E2E", fg="white", insertbackground="white"
)
task_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(app, bg="#1E1E1E")
button_frame.pack(pady=5)

# Add Task button
add_button = tk.Button(
    button_frame, text="Add Task", width=15, command=add_task,
    bg="#4CAF50", fg="white", activebackground="#45a049"
)
add_button.grid(row=0, column=0, padx=5)

# Remove Task button
remove_button = tk.Button(
    button_frame, text="Remove Task", width=15, command=remove_task,
    bg="#f44336", fg="white", activebackground="#e53935"
)
remove_button.grid(row=0, column=1, padx=5)

# Load tasks on startup
load_tasks()

# Run the app
app.mainloop()
