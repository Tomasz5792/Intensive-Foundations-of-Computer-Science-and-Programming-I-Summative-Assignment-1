
import random

def create_questions():
    questions = {}
    """
    Create a dictionarry of questions and answers for use in the gui.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    for i in range(1,10):
        x = random.randint(1,10)
        y = random.randint(1,20)
        z = random.randint(1,20)
        
        get_operator = lambda: ['+', '+', '-', '-', 'x', '%'][random.randint(0, 5)]
        operator = get_operator()

        if operator == '+':
            z = y + x
        elif operator == '-':
            z = y - x
        elif operator == 'x':
            z = y * x
        elif operator == '%':
            y = z * x

        questions["question_" + str(i)] = {
            "question_text":str(y)+" "+str(operator)+" X = "+str(z),
            "answer_text":str(y)+" "+str(operator)+" "+str(x)+" = "+str(z),
            "answer_no_x":"place_holder",
            "answer_correct?":"not_answered"
            }
        
        correct_answer_in_answers = False

        for answer in range(1,10):

            def create_answer(i: int, answer: int, x: int, is_correct_answer: bool=False):
                """
                Creates a correct or incorrect answer and adds it into the dictionarry.

                Args:
                    i (int): Index of the question in the questions dictionarry.
                    answer (int):  Index of the answer in the answers dictionarry.
                    x (int): The correct value of x.
                    is_correct_answer (bool, optinal): flags wether the returned answer should be correct or not.  Defaults to False.
                
                Returns:
                    None

                Raises:
                    None
                """
                if is_correct_answer:
                    questions["question_" + str(i)]["answers_" + str(answer)] = {
                        "answer_text": x,
                        "is_correct_answer" : True
                    }
                else:
                    operator = get_operator()
                    if operator == '+':
                        incorrect_answer = x + random.randint(1,20)
                    elif operator == '-':
                        incorrect_answer = x - random.randint(1,20)
                    elif operator == 'x':
                        incorrect_answer = x * random.randint(1,5) - random.randint(1,20)
                    elif operator == '%':
                        incorrect_answer = int( x / random.randint(1,5) - random.randint(1,20) )

                    if incorrect_answer == x:
                        incorrect_answer += 1

                    questions["question_" + str(i)]["answers_" + str(answer)] = {
                        "answer_text": incorrect_answer,
                        "is_correct_answer" : False
                    }                    

            if not correct_answer_in_answers and random.randint(1,9)==1:
                create_answer(i, answer, x, is_correct_answer=True)
                correct_answer_in_answers = True

            elif not correct_answer_in_answers and answer==9:
                create_answer(i, answer, x, is_correct_answer=True)
                correct_answer_in_answers = True

            else:
                create_answer(i, answer, x)

    
    return questions

data = create_questions()
print(data)