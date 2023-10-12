import tkinter as tk
from tkinter import messagebox
import random

# Function to load statements from the file
def load_statements(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        statements = file.readlines()
    return statements

# Function to check the user's answer
def check_answer():
    global correct_answers
    user_answer = entry.get().strip()

    if user_answer == statement_word:
        messagebox.showinfo("Correct!", "Correct answer!")
        correct_answers += 1
    else:
        messagebox.showerror("Wrong!", f"Wrong answer. The correct word (Odu) is: {statement_word}")
    
    next_statement()

# Function to display the next statement
def next_statement():
    global current_statement, statements, statement_word
    if current_statement < len(statements):
        statement = statements[current_statement].strip()
        number, statement_text = statement.split('. ', 1)
        statement_word = statement_text.split(' ', 1)[0]
        statement_text_hidden = statement_text.replace(statement_word, "[Hidden]", 1)

        label.config(text=f"Statement {number}: {statement_text_hidden}")
        entry.delete(0, tk.END)
        current_statement += 1
    else:
        messagebox.showinfo("Quiz Completed", f"You got {correct_answers} out of {len(statements)} words correct.")

# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x200")  # Set the fixed window size
root.configure(bg="#282828")  # Gruvbox background color

# Load statements
statements = load_statements("odus.txt")
random.shuffle(statements)
current_statement = 0
correct_answers = 0
statement_word = ""

# Create and configure GUI elements
label = tk.Label(
    root,
    text="",
    padx=10,
    pady=10,
    font=("Helvetica", 12),
    fg="#fbf1c7",  # Gruvbox foreground color
    bg="#282828",  # Gruvbox background color
)
label.pack()

entry = tk.Entry(
    root,
    font=("Helvetica", 12),
    bg="#282828",  # Gruvbox background color
    fg="#fbf1c7",  # Gruvbox foreground color
)
entry.pack()

check_button = tk.Button(
    root,
    text="Check Answer",
    command=check_answer,
    font=("Helvetica", 12),
    bg="#458588",  # Gruvbox highlight color
    fg="#fbf1c7",  # Gruvbox foreground color
)
check_button.pack()

next_statement()

root.mainloop()

