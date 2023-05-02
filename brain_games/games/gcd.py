from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'
START = 1
END = 1000


def play():
    randint_1 = randint(START, END)
    randint_2 = randint(START, END)
    question_text = f'{str(randint_1)} {str(randint_2)}'
    true_answer = gcd(randint_1, randint_2)
    return question_text, str(true_answer)
