import prompt

def structure(name_of_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(name_of_game.condition)
    i = 0

    for i in range(3):
        question, correct_answer = name_of_game.function()
        print(f'Question: {question}')
        answer = prompt.string('Your Answer: ')
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            return print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}. \nLet\'s try again, {name}!')
        else:
            return print(f'{answer} is wrong answer ;(.')
    print(f'Congratulations, {name}!')
