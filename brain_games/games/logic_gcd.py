from random import randint

CONDITION = 'Find the greatest common divisor of given numbers.'


def logic_game():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1} {number_2}'
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    correct_answer = str(number_1 + number_2)
    return question, correct_answer
