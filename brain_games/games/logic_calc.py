from random import randint
from random import choice
CONDITION = 'What is the result of the expression?'


def logic_game():
    string = ["+", "-", "*"]
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator = choice(string)
    question = f'{number_1} {operator} {number_2}'
    if operator == '+':
        correct_answer = str(number_1 + number_2)
    elif operator == '*':
        correct_answer = str(number_1 * number_2)
    elif operator == '-':
        correct_answer = str(number_1 - number_2)
    return question, correct_answer
