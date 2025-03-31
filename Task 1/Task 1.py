

import tkinter as tk

def handle_button_press(event):
    print("Button pressed!")

def create_gui():
    """
    Create a simple GUI

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.

    Raises:
        ValueError: If a or b are not integers.
    
    """
    root = tk.Tk()
    button = tk.Button(root, text="Click me")
    button2 = tk.Button(root, text="Click me")
    button.pack()
    button2.pack()

    # Bind the left mouse button click event to the handle_button_press function
    button.bind("<Button-1>", handle_button_press)

    root.mainloop()

create_gui()