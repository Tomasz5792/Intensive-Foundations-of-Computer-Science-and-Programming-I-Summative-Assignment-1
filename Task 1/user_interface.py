import tkinter as tk

root = tk.Tk()

def create_gui():
    """
    Create a simple GUI
    """
    root.title("Title")

    #row 1
    create_lable()

    #row 2
    button = create_button(1,1)
    button2 = create_button(1,2)
    button3 = create_button(1,3)

    #row 3
    button4 = create_button(2,1)
    button5 = create_button(2,2)
    button6 = create_button(2,3)

    #row 4
    button7 = create_button(3,1)
    button8 = create_button(3,2)
    button9 = create_button(3,3)

    #row 5


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

def create_lable():
    label = tk.Label(root, text="Click a button below!", font=("Arial", 14))
    label.grid(row=0, column=1, columnspan=3, pady=10, sticky="n")

def create_button(row: int, column: int):
    button = tk.Button(root, text="Click me", width=20, height=5)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", handle_button_press)
    return button

def handle_button_press(event):
    print("Button pressed!")

create_gui()
