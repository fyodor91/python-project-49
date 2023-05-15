from random import randint, choice


TASK = 'What is the result of the expression?'
START = 0
END = 1000


def get_question_answer():
    number_1 = randint(START, END)
    number_2 = randint(START, END)
    operators = '+', '-', '*'
    random_op = choice(operators)
    question_text = f'{number_1} {random_op} {number_2}'
    if random_op == '+':
        true_answer = number_1 + number_2
    elif random_op == '-':
        true_answer = number_1 - number_2
    elif random_op == '*':
        true_answer = number_1 * number_2
    return question_text, str(true_answer)
