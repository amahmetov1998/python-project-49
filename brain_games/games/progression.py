from random import randint


CONDITION = 'What number is missing in the progression?'


def make_round():
    number_1 = randint(1, 50)
    STEP = randint(1, 10)
    RANGE = randint(4, 9)
    list = [number_1]
    for _ in range(RANGE):
        number_1 = number_1 + STEP
        list.append(number_1)
    question = list
    number_2 = randint(0, len(list) - 1)
    correct_answer = str(question[number_2])
    list[number_2] = '..'
    for i in range(len(question)):
        question[i] = str(question[i])
    question = ' '.join(question)
    return question, correct_answer
