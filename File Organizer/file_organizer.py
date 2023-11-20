#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os  # Import the os module for operating system functionalities
import shutil  # Import the shutil module for high-level file operations
import tkinter as tk  # Import tkinter module for GUI
from tkinter import filedialog  # Import filedialog module for file-related dialog boxes

# Function to organize files into folders based on extension
def organize_files():
    # Retrieve the folder path entered in the entry field
    source_folder = entry.get()
    # Check if the entered path is valid
    if not os.path.exists(source_folder):
        status_label.config(text="Invalid directory!")
        return

    # Dictionary mapping file extensions to folder names
    extensions = {
        'txt': 'TextFiles',
        'pdf': 'PDFs',
        'jpg': 'Images',
        'png': 'Images',
        'xlsx': 'ExcelFiles',
        # Add more extensions and corresponding folder names as needed
    }

    # Create folders for each file extension if they don't exist
    for folder_name in extensions.values():
        folder_path = os.path.join(source_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Get a list of all files in the source directory
    files = [file for file in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, file))]

    # Organize files by moving them into respective folders based on extension
    for file in files:
        file_extension = file.split('.')[-1].lower()
        if file_extension in extensions:
            source_path = os.path.join(source_folder, file)
            destination_folder = os.path.join(source_folder, extensions[file_extension])
            destination_path = os.path.join(destination_folder, file)

            # Move the file to the appropriate folder
            shutil.move(source_path, destination_path)

    # Update the status label once the task is completed
    status_label.config(text="Task completed! Files organized.")

# Tkinter GUI setup
root = tk.Tk()  # Create the main window
root.title("File Organizer")  # Set the title for the window

# Label for folder path entry
label = tk.Label(root, text="Enter folder path:")  # Create a label
label.pack()  # Display the label in the window

# Entry field for folder path input
entry = tk.Entry(root, width=50)  # Create an entry field
entry.pack()  # Display the entry field in the window

# Button to browse and select folder using a file dialog
browse_button = tk.Button(root, text="Browse", command=lambda: entry.insert(tk.END, filedialog.askdirectory()))
# Create a button with a function to select a directory and insert its path into the entry field
browse_button.pack()  # Display the button in the window

# Button to trigger file organization process
organize_button = tk.Button(root, text="Organize Files", command=organize_files)  # Create a button to trigger file organization
organize_button.pack()  # Display the button in the window

# Status label to display completion message or errors
status_label = tk.Label(root, text="")  # Create a label for status messages
status_label.pack()  # Display the label in the window

# Start the Tkinter main loop
root.mainloop()  # Run the main loop to display the window and handle user interactions

