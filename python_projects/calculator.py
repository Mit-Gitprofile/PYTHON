import tkinter as tk

# Function to handle button click
def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the current entry field
    entry.insert(tk.END, current + char)  # Append the clicked button's value

# Function to evaluate the expression
def evaluate():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression and convert to string
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)  # Display the result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Show error in case of invalid input

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")

# Create the input field
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create and place the buttons
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=evaluate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Add Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the Tkinter event loop
root.mainloop()
