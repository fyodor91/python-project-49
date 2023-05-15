from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 0
END = 1000


def is_prime(value):
    if value == 0 or value == 1:
        return False
    i = 2
    while i < value:
        if value % i == 0:
            return False
        i += 1
    return True


def get_question_answer():
    random_value = randint(START, END)
    if is_prime(random_value):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question_text = str(random_value)
    return question_text, true_answer
