#!/usr/bin/env python3


import prompt
from random import randint
from math import gcd


def brain_gcd():
    exercise = 'Find the greatest common divisor of given numbers.'
    randint_1 = randint(0, 1000)
    randint_2 = randint(0, 1000)
    question_text = f'{str(randint_1)} {str(randint_2)}'
    true_answer = gcd(randint_1, randint_2)
    return exercise, (question_text, true_answer)


def wrong_answer(answer, true_answer):
    x = f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".'
    return x


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    exercise_text = brain_gcd()[0]
    print(exercise_text)
    i = 0
    while i < 3:
        question_text, true_answer = brain_gcd()[1]
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
