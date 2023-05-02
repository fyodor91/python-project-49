from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
END = 1000


def is_even(value):
    return value % 2 == 0


def play():
    random_value = randint(START, END)
    if is_even(random_value):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question_text = str(random_value)
    return question_text, true_answer
