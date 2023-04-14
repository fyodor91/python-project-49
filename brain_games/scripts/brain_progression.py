#!/usr/bin/env python3


import prompt
import random
import wrong_answer


def progression(begin, end, step):
    string = ''
    for i in range(begin, end, step):
        string += str(i) + ' '
    return string


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        begin_value = random.randint(1, 10)
        step_value = random.randint(1, 10)
        end_value = begin_value + step_value*9 + 1
        index_value = random.randint(0, 9)
        rprogression = progression(begin_value, end_value, step_value).split()
        true_answer = rprogression[index_value]
        progression_text = ' '.join(rprogression).replace(true_answer, '..', 1)
        print('Question: ' + str(progression_text))
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
