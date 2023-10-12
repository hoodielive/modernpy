# Initialize the GUI
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Rest of the script (unchanged)

# Create and configure GUI elements
root.configure(bg=COLOR_SCHEMES["Cappuccino"]["bg"])  # Set initial background color
frame = tk.Frame(root, bg=COLOR_SCHEMES["Cappuccino"]["bg"])  # Create a frame for centering
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

# Rest of the script (unchanged)

# Check Answer button as the default button
root.bind("<Return>", lambda event=None: check_button.invoke())

# Initial update of the tracker label and display the first statement
update_tracker()
next_statement()

root.mainloop()

