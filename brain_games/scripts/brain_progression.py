#!/usr/bin/env python3


import prompt
from random import randint


def progression(begin, end, step):
    string = ''
    for i in range(begin, end, step):
        string += str(i) + ' '
    return string


def brain_progression():
    exercise = 'What number is missing in the progression?'
    begin_value = randint(1, 10)
    step_value = randint(1, 10)
    end_value = begin_value + step_value*9 + 1
    index_value = randint(0, 9)
    rprogression = progression(begin_value, end_value, step_value).split()
    true_answer = rprogression[index_value]
    progression_text = ' '.join(rprogression).replace(true_answer, '..', 1)
    question_text = str(progression_text)
    return exercise, (question_text, true_answer)


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    exercise_text = brain_progression()[0]
    print(exercise_text)
    i = 0
    while i < 3:
        question_text, true_answer = brain_progression()[1]
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
            print(f"Let's try again, {name}!")
            break


if __name__ == '__main__':
    main()
