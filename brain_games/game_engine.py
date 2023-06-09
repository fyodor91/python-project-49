import prompt


WINS_COUNT = 3


def play_to_win(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    count = 0
    while count < WINS_COUNT:
        question_text, true_answer = game.get_question_answer()
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            count += 1
        else:
            print(f'"{answer}" is wrong answer ;(. \
Correct answer was "{true_answer}".')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
