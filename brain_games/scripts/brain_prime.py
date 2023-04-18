#!/usr/bin/env python3


import prompt
from random import randint


def is_prime(value):
    i = 1
    while i < value:
        if value % i == 0:
            return 'yes'
            break
        i += 1
    return 'no'


def brain_prime():
    exercise = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    value = randint(2, 1000)
    true_answer = is_prime(value)
    question_text = str(value)
    return exercise, (question_text, true_answer)


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    exercise_text = brain_prime()[0]
    print(exercise_text)
    i = 0
    while i < 3:
        question_text, true_answer = brain_prime()[1]
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if answer == str(true_answer):
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            (x, y) = (answer, true_answer)
            print(f'"{x}" is wrong answer ;(. Correct answer was "{y}".')
            print(f'Let's try again, {name}!')
            break


if __name__ == '__main__':
    main()
