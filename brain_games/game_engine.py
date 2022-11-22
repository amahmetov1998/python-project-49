import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.CONDITION)
    ROUNDS_COUNT = 3

    for i in range(ROUNDS_COUNT):
        question, correct_answer = game.make_round()
        print(f'Question: {question}')
        answer = prompt.string('Your Answer: ')
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            return print(f'{answer} is wrong answer ;(.'
                         f'Correct answer was {correct_answer}.'
                         f'\nLet\'s try again, {name}!')
        else:
            return print(f'{answer} is wrong answer ;(.')
    print(f'Congratulations, {name}!')
