from random import randint
from random import choice
condition = 'What is the result of the expression?'


def function():
    string = ["+", "-", "*"]
    NUMBER_1 = randint(1, 100)
    NUMBER_2 = randint(1, 100)
    operator = choice(string)
    question = f'{NUMBER_1} {operator} {NUMBER_2}'
    if operator == '+':
        correct_answer = str(NUMBER_1 + NUMBER_2)
    elif operator == '*':
        correct_answer = str(NUMBER_1 * NUMBER_2)
    elif operator == '-':
        correct_answer = str(NUMBER_1 - NUMBER_2)
    return question, correct_answer
