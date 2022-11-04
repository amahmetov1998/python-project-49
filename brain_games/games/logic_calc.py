from random import randint
from random import choice
import operator
condition = 'What is the result of the expression?'
dict1 = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}
def function():
    string = ["+","-","*"]
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator = choice(string)
    question = f'{number_1} {operator} {number_2}'
    correct_answer = number_1 operator number_2
    return question, correct_answer
