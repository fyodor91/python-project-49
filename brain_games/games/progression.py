from random import randint


TASK = 'What number is missing in the progression?'


def progression(begin, end, step):
    string = ''
    for i in range(begin, end, step):
        string += str(i) + ' '
    return string


def task():
    begin_value = randint(1, 10)
    step_value = randint(1, 10)
    end_value = begin_value + step_value * 9 + 1
    index_value = randint(0, 9)
    rprogression = progression(begin_value, end_value, step_value).split()
    true_answer = rprogression[index_value]
    progression_text = ' '.join(rprogression).replace(true_answer, '..', 1)
    question_text = str(progression_text)
    return question_text, true_answer
