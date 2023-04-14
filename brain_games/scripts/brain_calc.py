#!/usr/bin/env python3


import prompt
import random
import wrong_answer


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        randint_1 = random.randint(0, 1000)
        randint_2 = random.randint(0, 1000)
        operator_list = ['+', '-', '*']
        random_op = random.choice(operator_list)
        print(f'Question: {randint_1} {random_op} {randint_2}')
        answer = prompt.string('Your answer: ')
        if random_op == '+':
            true_answer = randint_1 + randint_2
            if int(answer) == true_answer:
                print('Correct!')
                i += 1
                if i == 3:
                    print('Congratulations, ' + name + '!')
            else:
                print(wrong_answer.main(answer, true_answer))
                print("Let's try again, " + name + "!")
                break
        elif random_op == '-':
            true_answer = randint_1 - randint_2
            if int(answer) == true_answer:
                print('Correct!')
                i += 1
                if i == 3:
                    print('Congratulations, ' + name + '!')
            else:
                print(wrong_answer.main(answer, true_answer))
                print("Let's try again, " + name + "!")
                break
        elif random_op == '*':
            true_answer = randint_1 * randint_2
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
