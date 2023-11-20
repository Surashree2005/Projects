import tkinter as tk  # Import the tkinter module and alias it as tk
import os  # Import the os module

# Function to display tasks in the listbox
def display_tasks():
    tasks_list.delete(0, tk.END)  # Delete existing tasks in the listbox
    if tasks:  # Check if tasks exist
        for task in tasks:  # Loop through tasks list
            tasks_list.insert(tk.END, task.strip())  # Insert each task into the listbox
    else:
        tasks_list.insert(tk.END, "No tasks found.")  # Display a message if no tasks are present

# Function to add a new task to the tasks list and update the display
def add_task():
    new_task = entry_task.get()  # Get the new task from the entry field
    if new_task:  # Check if a new task is provided
        tasks.append(new_task)  # Add the new task to the tasks list
        entry_task.delete(0, tk.END)  # Clear the entry field after adding the task
        display_tasks()  # Update the display in the listbox
        save_tasks_to_file()  # Save the updated tasks list to the file
        status_label.config(text="Task added successfully.", fg="green")  # Provide success message
    else:
        status_label.config(text="Please enter a task.", fg="red")  # Display error message if no task is entered

# Function to remove the selected task from the tasks list and update the display
def remove_task():
    selected_task = tasks_list.curselection()  # Get the index of the selected task
    if selected_task:  # Check if a task is selected
        index = selected_task[0]  # Get the index of the selected task
        del tasks[index]  # Remove the task from the tasks list
        display_tasks()  # Update the display in the listbox
        save_tasks_to_file()  # Save the updated tasks list to the file
        status_label.config(text="Task deleted.", fg="green")  # Provide deletion success message
    else:
        status_label.config(text="Please select a task to delete.", fg="red")  # Display error if no task is selected

# Function to save tasks to a file
def save_tasks_to_file():
    with open(file_name, "w") as file:  # Open the file in write mode
        for task in tasks:  # Loop through tasks list
            file.write(task + "\n")  # Write each task to the file with a newline

# Function to load tasks from a file
def load_tasks_from_file():
    if os.path.exists(file_name):  # Check if the file exists
        with open(file_name, "r") as file:  # Open the file in read mode
            return file.readlines()  # Return a list of tasks read from the file
    else:
        return []  # Return an empty list if the file doesn't exist

file_name = "tasks.txt"  # Set the filename for tasks data storage
tasks = load_tasks_from_file()  # Load tasks from the file (if the file exists)

root = tk.Tk()  # Create a Tkinter root window
root.title("Task Manager")  # Set the title of the window

frame_input = tk.Frame(root)  # Create a frame for input elements
frame_input.pack(padx=10, pady=10)  # Pack the frame into the root window

label_task = tk.Label(frame_input, text="Enter Task:")  # Create a label for task input
label_task.pack(side=tk.LEFT)  # Pack the label to the left side of the frame

entry_task = tk.Entry(frame_input, width=30)  # Create an entry field for task input
entry_task.pack(side=tk.LEFT, padx=5)  # Pack the entry field to the left of the frame with padding

button_add = tk.Button(frame_input, text="Add Task", command=add_task)  # Create a button to add tasks
button_add.pack(side=tk.LEFT, padx=5)  # Pack the button to the left of the frame with padding

# Create a frame for the tasks list and pack it into the root window
frame_list = tk.Frame(root)
frame_list.pack(padx=10, pady=5)

tasks_list = tk.Listbox(frame_list, width=40, height=10)  # Create a listbox to display tasks
tasks_list.pack(side=tk.LEFT, fill=tk.BOTH)  # Pack the listbox to the left side of the frame, fill it in both directions

scrollbar = tk.Scrollbar(frame_list)  # Create a scrollbar for the listbox
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Pack the scrollbar to the right side of the frame, fill in Y direction

tasks_list.config(yscrollcommand=scrollbar.set)  # Configure listbox to use scrollbar
scrollbar.config(command=tasks_list.yview)  # Configure scrollbar to control the listbox view

# Create a frame for buttons and status label, pack it into the root window
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=5)

button_remove = tk.Button(frame_buttons, text="Delete Task", command=remove_task)  # Create a button to delete tasks
button_remove.pack(side=tk.LEFT, padx=5)  # Pack the button to the left of the frame with padding

status_label = tk.Label(frame_buttons, text="", fg="black")  # Create a label for status messages
status_label.pack(side=tk.LEFT)  # Pack the label to the left side of the frame

display_tasks()  # Display tasks in the listbox when the program starts

root.mainloop()  # Start the Tkinter main event loop
