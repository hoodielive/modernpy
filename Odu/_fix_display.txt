# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Load statements
statements = load_statements("statements.txt")
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

# Initial update of the tracker label and display the first statement
update_tracker()
next_statement()

root.mainloop()

