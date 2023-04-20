from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def task():
    randint_1 = randint(0, 1000)
    randint_2 = randint(0, 1000)
    question_text = f'{str(randint_1)} {str(randint_2)}'
    true_answer = gcd(randint_1, randint_2)
    return question_text, true_answer
