from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(value):
    i = 2
    while i < value:
        if value % i == 0:
            return 'no'
            break
        i += 1
    return 'yes'


def task():
    value = randint(2, 1000)
    true_answer = is_prime(value)
    question_text = str(value)
    return question_text, true_answer
