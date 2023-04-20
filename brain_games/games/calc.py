from random import randint, choice


TASK = 'What is the result of the expression?'


def task():
    randint_1 = randint(0, 1000)
    randint_2 = randint(0, 1000)
    operator_list = ['+', '-', '*']
    random_op = choice(operator_list)
    question_text = f'{randint_1} {random_op} {randint_2}'
    if random_op == '+':
        true_answer = randint_1 + randint_2
    elif random_op == '-':
        true_answer = randint_1 - randint_2
    elif random_op == '*':
        true_answer = randint_1 * randint_2
    return question_text, true_answer
