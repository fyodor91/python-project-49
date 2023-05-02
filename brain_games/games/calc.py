from random import randint, choice


TASK = 'What is the result of the expression?'
START = 0
END = 1000


def play():
    randint_1 = randint(START, END)
    randint_2 = randint(START, END)
    operators = '+', '-', '*'
    random_op = choice(operators)
    question_text = f'{randint_1} {random_op} {randint_2}'
    if random_op == '+':
        true_answer = randint_1 + randint_2
    elif random_op == '-':
        true_answer = randint_1 - randint_2
    elif random_op == '*':
        true_answer = randint_1 * randint_2
    return question_text, str(true_answer)
