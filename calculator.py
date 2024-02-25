import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if current == "0":
        display_var.set(symbol)
    else:
        display_var.set(current + symbol)

def clear():
    display_var.set("0")

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widget to display the result
display_var = tk.StringVar()
display_var.set("0")
display = tk.Entry(root, textvariable=display_var, justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Clear button
clear_button = tk.Button(root, text="C", command=clear)
clear_button.grid(row=5, column=0, columnspan=2, sticky="nsew")

# Calculate button
calculate_button = tk.Button(root, text="=", command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, sticky="nsew")

# Configure grid weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
