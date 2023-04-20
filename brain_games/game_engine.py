import prompt


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    count = 0
    while count < 3:
        question_text, true_answer = game.task()
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if answer == str(true_answer):
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{answer}" is wrong answer ;(. \
Correct answer was "{true_answer}".')
            print(f"Let's try again, {name}!")
            break
