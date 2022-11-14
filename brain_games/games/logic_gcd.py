from random import randint

condition = 'Find the greatest common divisor of given numbers.'


def function():
    NUMBER_1 = randint(1, 100)
    NUMBER_2 = randint(1, 100)
    question = f'{NUMBER_1} {NUMBER_2}'
    while NUMBER_1 != 0 and NUMBER_2 != 0:
        if NUMBER_1 > NUMBER_2:
            NUMBER_1 = NUMBER_1 % NUMBER_2
        else:
            NUMBER_2 = NUMBER_2 % NUMBER_1
    correct_answer = str(NUMBER_1 + NUMBER_2)
    return question, correct_answer
