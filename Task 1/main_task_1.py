import tkinter as tk
from create_calculations import create_questions

root = tk.Tk()
root.title("Generates simple equation")

questions_correct = 0

def create_gui_questions(questions: dict, questions_correct: int):
    """
    Create a simple GUI with a 9 by 9 grid patern.

    Args:
        questions (dict):  Dictionarry of questions and answers for use with the gui
        questions_correct (int):  Used in number of questions correct label.

    Returns:
        None

    Raises:
        None
    """
 
    #row 1
    create_label(row=0,text="Click on a button to do a question.")

    #row 2
    if questions["question_1"]["answer_correct?"] == "not_answered":
        button = create_button(row=1, column=1, text=questions["question_1"]["question_text"], button_number=1)
    else:
        create_label_question(row=1, column=1, text=questions["question_1"]["question_text"]+"\n"+questions["question_1"]["answer_correct?"])

    if questions["question_2"]["answer_correct?"] == "not_answered":
        button = create_button(row=1, column=2, text=questions["question_2"]["question_text"], button_number=2)
    else:
        create_label_question(row=1, column=2, text=questions["question_2"]["question_text"]+"\n"+questions["question_2"]["answer_correct?"])

    if questions["question_3"]["answer_correct?"] == "not_answered":
        button = create_button(row=1, column=3, text=questions["question_3"]["question_text"], button_number=3)
    else:
        create_label_question(row=1, column=3, text=questions["question_3"]["question_text"]+"\n"+questions["question_3"]["answer_correct?"])

    # row 3
    if questions["question_4"]["answer_correct?"] == "not_answered":
        button = create_button(row=2, column=1, text=questions["question_4"]["question_text"], button_number=4)
    else:
        create_label_question(row=2, column=1, text=questions["question_4"]["question_text"] + "\n" + questions["question_4"]["answer_correct?"])

    if questions["question_5"]["answer_correct?"] == "not_answered":
        button = create_button(row=2, column=2, text=questions["question_5"]["question_text"], button_number=5)
    else:
        create_label_question(row=2, column=2, text=questions["question_5"]["question_text"] + "\n" + questions["question_5"]["answer_correct?"])

    if questions["question_6"]["answer_correct?"] == "not_answered":
        button = create_button(row=2, column=3, text=questions["question_6"]["question_text"], button_number=6)
    else:
        create_label_question(row=2, column=3, text=questions["question_6"]["question_text"] + "\n" + questions["question_6"]["answer_correct?"])

    # row 4
    if questions["question_7"]["answer_correct?"] == "not_answered":
        button = create_button(row=3, column=1, text=questions["question_7"]["question_text"], button_number=7)
    else:
        create_label_question(row=3, column=1, text=questions["question_7"]["question_text"] + "\n" + questions["question_7"]["answer_correct?"])

    if questions["question_8"]["answer_correct?"] == "not_answered":
        button = create_button(row=3, column=2, text=questions["question_8"]["question_text"], button_number=8)
    else:
        create_label_question(row=3, column=2, text=questions["question_8"]["question_text"] + "\n" + questions["question_8"]["answer_correct?"])

    if questions["question_9"]["answer_correct?"] == "not_answered":
        button = create_button(row=3, column=3, text=questions["question_9"]["question_text"], button_number=9)
    else:
        create_label_question(row=3, column=3, text=questions["question_9"]["question_text"] + "\n" + questions["question_9"]["answer_correct?"])

    #row 5
    create_label(row=4,columnspan=2,text="Questions correct "+str(questions_correct)+"/9")
    button = create_button(row=4,column=3,height=1,text="Reset",button_type="reset")

    #app layout
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


def create_gui_answer(questions: dict, int_question_selected: int, questions_correct: int):
    """
    Create a simple GUI to allow the user to pick an answer.

    Args:
        questions (dict):  Dictionarry of questions and answers for use with the gui.
        int_question_selected (int): Number of question selected.
        questions_correct (int):  Used in number of questions correct label.

    Returns:
        None

    Raises:
        None
    """
    string_question_selected = "question_" + str(int_question_selected)

    #row 1
    create_label(row=0,text="     Question to answer: " + questions[string_question_selected]["question_text"]+"     ")

    #row 2
    button = create_button(row=1, column=1, text=questions[string_question_selected]['answers_1']['answer_text'], button_number=1,button_type="answer",int_question_selected=int_question_selected)
    button = create_button(row=1,column=2, text=questions[string_question_selected]['answers_2']['answer_text'], button_number=2,button_type="answer",int_question_selected=int_question_selected)
    button = create_button(row=1,column=3, text=questions[string_question_selected]['answers_3']['answer_text'], button_number=3,button_type="answer",int_question_selected=int_question_selected)

    #row 3
    button = create_button(row=2,column=1, text=questions[string_question_selected]['answers_4']['answer_text'], button_number=4,button_type="answer",int_question_selected=int_question_selected)
    button = create_button(row=2,column=2, text=questions[string_question_selected]['answers_5']['answer_text'], button_number=5,button_type="answer",int_question_selected=int_question_selected)
    button = create_button(row=2,column=3, text=questions[string_question_selected]['answers_6']['answer_text'], button_number=6,button_type="answer",int_question_selected=int_question_selected)

    #row 4
    button = create_button(row=3,column=1, text=questions[string_question_selected]['answers_7']['answer_text'], button_number=7,button_type="answer",int_question_selected=int_question_selected)
    button = create_button(row=3,column=2, text=questions[string_question_selected]['answers_8']['answer_text'], button_number=8,button_type="answer",int_question_selected=int_question_selected)
    button = create_button(row=3,column=3, text=questions[string_question_selected]['answers_9']['answer_text'], button_number=9,button_type="answer",int_question_selected=int_question_selected)

    #row 5
    create_label(row=4,columnspan=2,text="Questions correct "+str(questions_correct)+"/9")
    button = create_button(row=4,column=3,height=1,text="Back",button_type="back")

    #app layout
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


def create_label(row: int,columnspan: int=3, text: str="Error"):
    """
    Create title label for gui.

    Args:
        row: (int): The row the label is created on.
        columnspan (int, optional): The amount of columns the label spans. Defaults to 3.
        text (str): Text for the box.  Defaults to Error.

    Returns:
        None

    Raises:
        None
    """
    label = tk.Label(root, text=text, font=("Arial", 14))
    label.grid(row=row, column=1, columnspan=columnspan, pady=10, sticky="n")


def create_label_question(row: int, column: int, text: str="Error"):
    """
    Create label for gui to show answered questions

    Args:
        row: (int): The row the label is created on.
        column: (int): The column the label is created on.
        text (str): Text for the box.  Defaults to Error.

    Returns:
        None

    Raises:
        None
    """
    label = tk.Label(root, text=text, font=("Arial", 14))
    label.grid(row=row, column=column, pady=10, sticky="n")


def create_button(row: int, column: int, int_question_selected: int=0, button_number: int=0, width: int=20, height: int=5, text: str="Error", button_type: str="calculation"):
    """
    Create button for gui

    Args:
        row: (int): The row the button is created on.
        column: (int): The column the button is created on.
        int_question_selected (int): The question that was selected.  Defaults to zero.
        button_number: (int): The buttons number, used in functions.  Defaults to 0.
        width: (int, optional): The width of the button.  Defaults to 20.
        height: (int, optional): The height of the button.  Defaults to 5.
        text (str, optional): Text for the box.  Defaults to Error.
        button_type: (str, optional): The type of function the button runs.  Defaults to "calculation".

    Returns:
        tk.Button: The created button widget.

    Raises:
        None
    """
    button = tk.Button(root, text=text, width=width, height=height)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    if button_type == "reset":
        button.bind("<Button-1>", handle_button_press_reset)
    elif button_type == "back":
        button.bind("<Button-1>", handle_button_press_back)
    elif button_type == "calculation":
        button.bind("<Button-1>", lambda event: handle_button_press_select_question(event, button_number))
    elif button_type == "answer":
        button.bind("<Button-1>", lambda event: handle_button_press_select_answer(event, button_number,int_question_selected))
    else:
        button.bind("<Button-1>", lambda event: handle_button_press(event, row, column, button_number))
    
    return button


def handle_button_press(event, row, column, button_number):
    """
    Handles button press event
    """
    print(f"Button {button_number} row: {row} coumn: {column} was pressed.")


def handle_button_press_select_question(event, button_number):
    """
    Handles button press event
    """
    print(f"Question.  Button {button_number} was pressed.")
    int_question_selected = button_number
    create_gui_answer(questions, int_question_selected, questions_correct)


def handle_button_press_select_answer(event, button_number, int_question_selected):
    """
    Handles button press event
    """
    #global questions  #seems to be erroring linting.  Works without check why later.
    global questions_correct
    string_question_selected = "question_" + str(int_question_selected)
    string_answer_selected = "answers_" + str(button_number)
    bool_is_correct = questions[string_question_selected]["int_answer_x"] == questions[string_question_selected][string_answer_selected]['answer_text']
    print(f"Answer.  Button: {button_number}.  Question number: {int_question_selected}.")
    print(f"Question: "+questions[string_question_selected]["question_text"]+" Answer: "+str(questions[string_question_selected]["int_answer_x"]))
    print(f"Answer selected: "+str(questions[string_question_selected][string_answer_selected]['answer_text'])+" Is correct? "+str(bool_is_correct))
    if bool_is_correct:
        questions[string_question_selected]["answer_correct?"] = "Correct"
        questions_correct = questions_correct + 1
    else:
        questions[string_question_selected]["answer_correct?"] = "Incorrect"
    clear_root()
    create_gui_questions(questions, questions_correct)


def handle_button_press_reset(event):
    """
    Handles button press reset event
    """
    print("Reset was pressed")
    #resets questions and questions correct globally
    global questions, questions_correct
    questions = create_questions()
    questions_correct = 0
    clear_root()
    create_gui_questions(questions,questions_correct)


def handle_button_press_back(event):
    """
    Handles button press back event
    """
    print("Reset was pressed")
    clear_root()
    create_gui_questions(questions,questions_correct)


def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

questions = create_questions()

create_gui_questions(questions,questions_correct)

