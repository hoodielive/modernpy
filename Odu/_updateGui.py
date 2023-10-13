import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Create a ThemedStyle instance and set a modern theme (e.g., "plastik")
style = ThemedStyle(root)
style.set_theme("plastik")

# Rest of the code (unchanged)

# Create and configure GUI elements using ttk widgets
frame = ttk.Frame(root, padding=10)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

label = ttk.Label(
    frame,
    text="",
    font=("Helvetica", 12),
    wraplength=600,  # Adjust text wrapping
)
label.pack()

entry = ttk.Entry(
    frame,
    font=("Helvetica", 12),
    width=50,  # Adjust entry width
)
entry.pack()

check_button = ttk.Button(
    frame,
    text="Check Answer",
    command=check_answer,
    style="TButton",  # Use the default ttk button style
)
check_button.pack()

result_label = ttk.Label(
    frame,
    text="",
    font=("Helvetica", 12),
)
result_label.pack()

# Rest of the code (unchanged)

root.mainloop()

