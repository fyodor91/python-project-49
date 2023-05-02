from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 2
END = 1000


def is_prime(value):
    i = 2
    while i < value:
        if value % i == 0:
            return False
            break
        i += 1
    return True


def play():
    random_value = randint(START, END)
    if is_prime(random_value):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question_text = str(random_value)
    return question_text, true_answer
