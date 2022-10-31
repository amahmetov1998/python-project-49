import prompt
import brain_games.games.logic_even

def even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    for i in range(3):
        answer = prompt.string(f'Question: {brain_games.games.logic_even.random_number}\nYour Answer: ')
        if answer == brain_games.games.logic_even.correct_answer:
            print('Correct!')
        elif answer != brain_games.games.logic_even.correct_answer:
            return print(f'{answer} is wrong answer ;(. Correct answer was {brain_games.games.logic_even.correct_answer}.')
        else:
            return print(f'{answer} is wrong answer ;(.')
    print(f'Congratulations, {name}!')

