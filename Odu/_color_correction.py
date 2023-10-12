import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

# Color schemes
COLOR_SCHEMES = {
    "Gruvbox": {
        "bg": "#282828",
        "fg": "#fbf1c7",
        "highlight_bg": "#458588",
        "label_fg": "#fbf1c7",
        "entry_bg": "#282828",
        "entry_fg": "#fbf1c7",
    },
    "Ayu-Dark": {
        "bg": "#1e1e1e",
        "fg": "#c7c7c7",
        "highlight_bg": "#528bff",
        "label_fg": "#c7c7c7",
        "entry_bg": "#1e1e1e",
        "entry_fg": "#c7c7c7",
    },
    "Ayu-Light": {
        "bg": "#f3f3f3",
        "fg": "#525252",
        "highlight_bg": "#528bff",
        "label_fg": "#525252",
        "entry_bg": "#f3f3f3",
        "entry_fg": "#525252",
    },
    "Cappuccino": {
        "bg": "#e0e0e0",
        "fg": "#000000",  # Change text color to black for visibility
        "highlight_bg": "#b16286",
        "label_fg": "#000000",  # Change text color to black for visibility
        "entry_bg": "#e0e0e0",
        "entry_fg": "#000000",  # Change text color to black for visibility
    },
}

# Function to load statements from the file
def load_statements(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        statements = file.readlines()
    return statements

# Rest of the script (unchanged)

# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Rest of the script (unchanged)

# Initial update of the tracker label
update_tracker()

root.mainloop()

