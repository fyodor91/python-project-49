import prompt


WIN_COUNT = 3


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    count = 0
    while count < WIN_COUNT:
        question_text, true_answer = game.play()
        print(f'Question: {question_text}')
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            count += 1
            if count == WIN_COUNT:
                print(f'Congratulations, {name}!')
        else:
            print(f'"{answer}" is wrong answer ;(. \
Correct answer was "{true_answer}".')
            print(f"Let's try again, {name}!")
            break
