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

# Function to check the user's answer
def check_answer():
    global correct_answers, wrong_answers
    user_answer = entry.get().strip()

    if user_answer == statement_word:
        correct_answers += 1
        result_label.config(text="Correct!", fg="green")
    else:
        wrong_answers += 1
        result_label.config(text=f"Wrong. The correct Odu is: {statement_word}", fg="red")

    next_statement()

# Function to display the next statement
def next_statement():
    global current_statement, statements, statement_word, queries_left
    if current_statement < len(statements):
        statement = statements[current_statement].strip()
        number, statement_text = statement.split('. ', 1)
        statement_word = statement_text.split(' ', 1)[0]
        statement_text_hidden = statement_text.replace(statement_word, "[Hidden]", 1)

        label.config(text=f"Oracle #{number}: {statement_text_hidden}")
        entry.delete(0, tk.END)
        current_statement += 1
        queries_left -= 1
        update_tracker()
    else:
        result_label.config(text=f"Quiz Completed! You got {correct_answers} correct and {wrong_answers} wrong.", fg="blue")

# Function to update the tracker label
def update_tracker():
    tracker_label.config(text=f"Queries Left: {queries_left} | Correct: {correct_answers} | Wrong: {wrong_answers}")

# Function to change the color scheme
def change_color_scheme(event):
    selected_scheme = color_scheme_combo.get()
    if selected_scheme in COLOR_SCHEMES:
        scheme = COLOR_SCHEMES[selected_scheme]
        root.configure(bg=scheme["bg"])
        label.configure(fg=scheme["fg"], bg=scheme["bg"])
        entry.configure(bg=scheme["entry_bg"], fg=scheme["entry_fg"])
        check_button.configure(bg=scheme["highlight_bg"])
        tracker_label.configure(fg=scheme["label_fg"])

# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Load statements
statements = load_statements("odus.txt")
random.shuffle(statements)
current_statement = 0
correct_answers = 0
wrong_answers = 0
statement_word = ""
queries_left = len(statements)

# Create and configure GUI elements
root.configure(bg=COLOR_SCHEMES["Cappuccino"]["bg"])  # Set initial background color
frame = tk.Frame(root, bg=COLOR_SCHEMES["Cappuccino"]["bg"])  # Create a frame for centering
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame
label = tk.Label(
    frame,
    text="",
    padx=10,
    pady=10,
    font=("Helvetica", 12),
    fg=COLOR_SCHEMES["Cappuccino"]["fg"],
    bg=COLOR_SCHEMES["Cappuccino"]["bg"],
    wraplength=600,  # Adjust text wrapping
)
label.pack()

entry = tk.Entry(
    frame,
    font=("Helvetica", 12),
    bg=COLOR_SCHEMES["Cappuccino"]["entry_bg"],
    fg=COLOR_SCHEMES["Cappuccino"]["entry_fg"],
    width=50,  # Adjust entry width
)
entry.pack()

check_button = tk.Button(
    frame,
    text="Check Answer",
    command=check_answer,
    font=("Helvetica", 12),
    bg=COLOR_SCHEMES["Cappuccino"]["highlight_bg"],
    fg=COLOR_SCHEMES["Cappuccino"]["fg"],
)
check_button.pack()

result_label = tk.Label(
    frame,
    text="",
    font=("Helvetica", 12),
    fg="green",  # Default color for feedback
    bg=COLOR_SCHEMES["Cappuccino"]["bg"],
)
result_label.pack()

# Tracker label in the top right corner
tracker_label = tk.Label(
    root,
    text="Queries Left: 256 | Correct: 0 | Wrong: 0",  # Default values
    font=("Helvetica", 10),
    fg=COLOR_SCHEMES["Cappuccino"]["label_fg"],
    bg=COLOR_SCHEMES["Cappuccino"]["bg"],
    anchor="e",  # Right-align the text
)
tracker_label.place(relx=1.0, rely=0.0, anchor="ne")  # Top right corner

# Dropdown menu for changing color schemes
color_scheme_label = tk.Label(
    root,
    text="Select Color Scheme:",
    font=("Helvetica", 10),
    fg=COLOR_SCHEMES["Cappuccino"]["label_fg"],
    bg=COLOR_SCHEMES["Cappuccino"]["bg"],
)
color_scheme_label.place(relx=0.0, rely=0.0, anchor="nw")  # Top left corner

color_schemes = list(COLOR_SCHEMES.keys())
color_scheme_combo = ttk.Combobox(
    root,
    values=color_schemes,
    state="readonly",
    font=("Helvetica", 10),
)
color_scheme_combo.set("Cappuccino")  # Set default color scheme
color_scheme_combo.place(relx=0.15, rely=0.0, anchor="nw")  # Top left corner

color_scheme_combo.bind("<<ComboboxSelected>>", change_color_scheme)  # Bind event handler

# Check Answer button as the default button
root.bind("<Return>", lambda event=None: check_button.invoke())

# Initial update of the tracker label and display the first statement
update_tracker()
next_statement()

root.mainloop()

