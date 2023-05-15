from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 1000


def is_even(value):
    return value % 2 == 0


def get_question_answer():
    number = randint(START, END)
    if is_even(number):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question_text = str(number)
    return question_text, true_answer
