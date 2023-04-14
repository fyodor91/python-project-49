#!/usr/bin/env python3


import prompt
import random
import wrong_answer


def is_prime(value):
    i = 1
    while i < value:
        if value % i == 0:
            return 'no'
            break
        i += 1
    return 'yes'


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        value = random.randint(2, 1000)
        print('Question: ' + str(value))
        true_answer = is_prime(value)
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print('Congratulations, ' + name + '!')
        else:
            print(wrong_answer.main(answer, true_answer))
            print("Let's try again, " + name + "!")
            break


if __name__ == '__main__':
    main()
