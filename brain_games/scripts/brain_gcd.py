#!/usr/bin/env python3


import prompt
import random
import math
import wrong_answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        randint_1 = random.randint(0, 1000)
        randint_2 = random.randint(0, 1000)
        print('Question: ' + str(randint_1) + ' ' + str(randint_2))
        answer = prompt.string('Your answer: ')
        true_answer = math.gcd(randint_1, randint_2)
        if int(answer) == true_answer:
            print('Correct!')
            i += 1
            if i == 3:
                print('Congratulations, ' + name + '!')
        else:
            print(wrong_answer.main(answer, true_answer))
            print("Let's try again, " + name + "!")
            break


if __name__ == '__main__':
    main()
