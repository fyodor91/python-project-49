from random import randint


TASK = 'What number is missing in the progression?'
START = 1
END = 10
INDEX_START = 0
INDEX_END = 9
REPLACE_INDEX = 1
INDEX_CORRECTION = 1


def progression(begin, end, step):
    string = ''
    for i in range(begin, end, step):
        string += str(i) + ' '
    return string


def play():
    begin_value = randint(START, END)
    step_value = randint(START, END)
    end_value = begin_value + step_value * (INDEX_END - INDEX_START) + INDEX_CORRECTION
    index_value = randint(INDEX_START, INDEX_END)
    random_progression = progression(begin_value, end_value, step_value).split()
    true_answer = random_progression[index_value]
    progression_text = ' '.join(random_progression).replace(true_answer, '..', REPLACE_INDEX)
    question_text = str(progression_text)
    return question_text, str(true_answer)
