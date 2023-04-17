#!/usr/bin/env python3


import prompt
from random import randint
from random import choice


def brain_calc():
    exercise = 'What is the result of the expression?'
    randint_1 = randint(0, 1000)
    randint_2 = randint(0, 1000)
    operator_list = ['+', '-', '*']
    random_op = choice(operator_list)
    question_text = f'Question: {randint_1} {random_op} {randint_2}'
    if random_op == '+':
        true_answer = randint_1 + randint_2
    elif random_op == '-':
        true_answer = randint_1 - randint_2
    elif random_op == '*':
        true_answer = randint_1 * randint_2
    return exercise, (question_text, true_answer)


def wrong_answer(answer, true_answer):
    x = f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".'
    return x


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    exercise_text = brain_calc()[0]
    print(exercise_text)
    i = 0
    while i < 3:
        question_text, true_answer = brain_calc()[1]
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if answer == str(true_answer):
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(wrong_answer(answer, true_answer))
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
