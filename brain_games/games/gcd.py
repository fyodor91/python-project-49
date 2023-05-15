from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'
START = 1
END = 1000


def get_question_answer():
    number_1 = randint(START, END)
    number_2 = randint(START, END)
    question_text = f'{str(number_1)} {str(number_2)}'
    true_answer = gcd(number_1, number_2)
    return question_text, str(true_answer)
