import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASK_FILE = "Completed\To-Do-List\list.txt"

# List to store tasks and their check states
tasks = []
task_vars = []

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

# Function to capitalize task text
def capitalizer(task):
    return task.strip().capitalize()

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task = capitalizer(task)  # Capitalize the task
        tasks.append(task)
        task_vars.append(tk.BooleanVar(value=False))  # Add unselected checkbox
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        # Create a frame for each task
        task_item_frame = tk.Frame(task_frame, bg="#1E1E1E")
        task_item_frame.pack(fill="x", pady=2)

        # Checkbox for marking task completion
        checkbox = tk.Checkbutton(
            task_item_frame,
            variable=task_vars[i],
            fg="lime",
            bg="#1E1E1E",
            selectcolor="#1E1E1E",
            activebackground="#1E1E1E",
            font=("Arial", 10)
        )
        checkbox.pack(side="left")

        # Create a label for the text
        label = tk.Label(
            task_item_frame,
            text=task,
            fg="white",
            bg="#1E1E1E",
            font=("Arial", 10),
            anchor="w"
        )
        label.pack(side="left", fill="x", expand=True)

        # Create a context menu for each task
        menu = tk.Menu(
            app, 
            tearoff=0, 
            bg="#1E1E1E", 
            fg="red", 
            borderwidth=0, 
            relief="flat"
        )
        menu.add_command(
            label="Delete", 
            command=lambda task_index=i: delete_task(task_index), 
            background="#1E1E1E", 
            foreground="red", 
            activebackground="#333333", 
            activeforeground="red"
        )

        # Bind right-click to the label only
        label.bind("<Button-3>", lambda event, task_menu=menu: task_menu.tk_popup(event.x_root, event.y_root))

# Function to delete a task
def delete_task(task_index):
    del tasks[task_index]
    del task_vars[task_index]
    update_task_list()


# Function to exit the app
def exit_app():
    save_tasks()
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
app.configure(bg="#1E1E1E", bd=1, highlightthickness="1")

# Make the window transparent when it loses focus
def on_focus_out(event):
    app.wm_attributes("-alpha", 0.5)
    app.configure(highlightthickness=0)

def on_focus_in(event):
    app.wm_attributes("-alpha", 1.0)
    app.configure(highlightthickness=1)

# Bind focus events
app.bind("<FocusOut>", on_focus_out)
app.bind("<FocusIn>", on_focus_in)

# Input and Button Frame
input_button_frame = tk.Frame(app, bg="#1E1E1E")
input_button_frame.pack(pady=5, padx=5, fill="x")

# Input Field with Underline
input_frame = tk.Frame(input_button_frame, bg="#1E1E1E")
input_frame.pack(
    side="right",
    expand=True,
    fill="x",
    padx=(0, 5)
)

# Input Field with Enhanced Styling
task_entry = tk.Entry(
    input_frame,
    width=20,
    bg="#1E1E1E",
    fg="white",
    insertbackground="white",
    borderwidth=0,
    font=("Arial", 12),
    highlightthickness=1,
    highlightbackground="#555555",
    highlightcolor="#00FF00",
    relief="flat"
)
task_entry.pack(side="top", pady=5, padx=5, ipadx=5)

# Bind the Enter key to the add_task function
task_entry.bind("<Return>", lambda event: add_task())

# Exit Button
exit_button = tk.Button(
    input_button_frame,
    text="❌",
    command=exit_app,
    bg="#1E1E1E",
    fg="lime",
    activeforeground="red",
    activebackground="#1E1E1E",
    borderwidth=0,
    relief="flat"
)
exit_button.pack(side="left")

# Task List Display
task_frame = tk.Frame(app, bg="#1E1E1E")
task_frame.pack(
    padx=2, 
    pady=0, 
    fill="both", 
    expand=True
)

# Load tasks on startup
load_tasks()

# Run the app
app.mainloop()