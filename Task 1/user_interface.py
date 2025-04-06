import tkinter as tk



root = tk.Tk()

def create_gui():
    """
    Create a simple GUI

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    root.title("Title")

    #row 1
    create_label(row=0)

    #row 2
    button = create_button(row=1,column=1)
    button2 = create_button(row=1,column=2)
    button3 = create_button(row=1,column=3)

    #row 3
    button = create_button(row=2,column=1)
    button2 = create_button(row=2,column=2)
    button3 = create_button(row=2,column=3)

    #row 4
    create_label(row=3,columnspan=2)
    button3 = create_button(row=3,column=3,height=1)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)

    root.mainloop()

def create_label(row: int,columnspan: int=3):
    """
    Create lable for gui

    Args:
        row: (int): The row the label is created on.
        columnspan (int, optional): The amount of columns the label spans. Defaults to 3.

    Returns:
        None

    Raises:
        None
    """
    label = tk.Label(root, text="Click a button below!", font=("Arial", 14))
    label.grid(row=row, column=1, columnspan=columnspan, pady=10, sticky="n")

def create_button(row: int, column: int, width: int=20, height: int=5):
    """
    Create button for gui

    Args:
        row: (int): The row the button is created on.
        column: (int): The column the button is created on.
        width: (int, optional): The width of the button.  Defaults to 20.
        height: (int, optional): The height of the button.  Defaults to 5.

    Returns:
        tk.Button: The created button widget.

    Raises:
        None
    """
    button = tk.Button(root, text="Click me", width=width, height=height)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", lambda event: handle_button_press(event, row, column))
    return button

def handle_button_press(event, row, column):
    """
    Handles button press event
    """
    print(f"Button row: {row} coumn: {column} was pressed.")


create_gui()
