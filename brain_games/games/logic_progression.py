from random import randint


condition = 'What number is missing in the progression?'


def function():
    NUMBER_1 = randint(1, 50)
    STEP = randint(1, 10)
    RANGE = randint(4, 9)
    list = [NUMBER_1]
    for _ in range(RANGE):
        NUMBER_1 = NUMBER_1 + STEP
        list.append(NUMBER_1)
    question = list
    NUMBER_2 = randint(0, len(list) - 1)
    correct_answer = str(question[NUMBER_2])
    list[NUMBER_2] = '..'
    for i in range(len(question)):
        question[i] = str(question[i])
    question = ' '.join(question)
    return question, correct_answer
