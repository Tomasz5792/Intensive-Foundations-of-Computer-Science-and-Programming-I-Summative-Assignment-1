

import tkinter as tk

def handle_button_press(event):
    print("Button pressed!")

def create_gui():
    """
    Create a simple GUI
    
    
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