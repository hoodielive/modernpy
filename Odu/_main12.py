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
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Load statements
statements = load_statements("odus.txt")
random.shuffle(statements)
current_statement = 0
correct_answers = 0
statement_word = ""

# Create and configure GUI elements
root.configure(bg="#e0e0e0")  # Set background color to cappuccino

frame = tk.Frame(root, bg="#e0e0e0")  # Create a frame for centering
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

label = tk.Label(
    frame,
    text="",
    padx=10,
    pady=10,
    font=("Helvetica", 12),
    fg="#3a3a3a",  # Set the text color to match cappuccino
    bg="#e0e0e0",  # Set the background color to cappuccino
)
label.pack()

entry = tk.Entry(
    frame,
    font=("Helvetica", 12),
    bg="#e0e0e0",  # Set the background color to cappuccino
    fg="#3a3a3a",  # Set the text color to match cappuccino
)
entry.pack()

check_button = tk.Button(
    frame,
    text="Check Answer",
    command=check_answer,
    font=("Helvetica", 12),
    bg="#b16286",  # Set the button color to match cappuccino
    fg="#e0e0e0",  # Set the text color to match cappuccino
)
check_button.pack()

next_statement()

root.mainloop()

