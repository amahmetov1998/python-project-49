from random import randint

CONDITION = 'Find the greatest common divisor of given numbers.'


def find_gcd(number_1, number_2):
    while number_1 != 0 and number_2 != 0:
        if number_1 > number_2:
            number_1 = number_1 % number_2
        else:
            number_2 = number_2 % number_1
    number_3 = number_1 + number_2
    return number_3


def make_round():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1} {number_2}'
    correct_answer = str(find_gcd(number_1, number_2))
    return question, correct_answer
