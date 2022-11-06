from random import randint, choice

condition = 'What number is missing in the progression?'


def function():
    a = randint(1, 50)
    step = randint(1, 10)
    range_1 = randint(4, 9)
    list = [a]
    for _ in range(range_1):
        a = a + step
        list.append(a)
    question = list
    random_number = randint(0,len(list)-1)
    correct_answer = str(list[random_number])
    list[random_number] = '..'
    return question, correct_answer
