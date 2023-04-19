from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".' 


def task():
    random_value = randint(0, 1000)
    if random_value % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question_text = str(random_value)
    return question_text, true_answer
