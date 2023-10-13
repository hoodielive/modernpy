import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style  # Import Style from ttkbootstrap

# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Create a Style instance and set a Bootstrap theme (e.g., "flatly")
style = Style(theme="flatly")  # Use "flatly" or choose another Bootstrap theme

# Rest of the code (unchanged)

# Create and configure GUI elements using ttk widgets with ttkbootstrap styling
frame = ttk.Frame(root, padding=10, style="Frame.TFrame")
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

label = ttk.Label(
    frame,
    text="",
    font=("Helvetica", 12),
    style="Label.TLabel",
    wraplength=600,  # Adjust text wrapping
)
label.pack()

entry = ttk.Entry(
    frame,
    font=("Helvetica", 12),
    style="Entry.TEntry",
    width=50,  # Adjust entry width
)
entry.pack()

check_button = ttk.Button(
    frame,
    text="Check Answer",
    command=check_answer,
    style="TButton",
)
check_button.pack()

result_label = ttk.Label(
    frame,
    text="",
    font=("Helvetica", 12),
    style="ResultLabel.TLabel",
)
result_label.pack()

# Rest of the code (unchanged)

root.mainloop()
