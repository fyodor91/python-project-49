#!/usr/bin/env python3


import prompt
from random import randint


def brain_even():
    exercise = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_value = randint(0, 1000)
    if random_value % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question_text = str(random_value)
    return exercise, (question_text, true_answer)



def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    exercise_text = brain_even()[0]
    print(exercise_text)
    i = 0
    while i < 3:
        question_text, true_answer = brain_even()[1]
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".')
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
