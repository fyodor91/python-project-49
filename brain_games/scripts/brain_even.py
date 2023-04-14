#!/usr/bin/env python3


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_value = random.randint(0, 1000)
        print('Question: ' + str(random_value))
        answer = prompt.string('Your answer: ')
        if random_value % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                i += 1
                if i == 3:
                    print('Congratulations, ' + name + '!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again, " + name + "!")
                break
        else:
            if answer == 'no':
                print('Correct!')
                i += 1
                if i == 3:
                    print('Congratulations, ' + name + '!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, " + name + "!")
                break


if __name__ == '__main__':
    main()
