import prompt
from brain_games.games.logic_even import random_number, correct_answer

def even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    for i in range(3):
        answer = prompt.string(f'Question: {random_number}\nYour Answer: ')
        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            return print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
        else:
            return print(f'{answer} is wrong answer ;(.')
    print(f'Congratulations, {name}!')

