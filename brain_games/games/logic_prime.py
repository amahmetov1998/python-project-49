from random import randint

condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def function_1(question):
    if question < 2:
        return False
    for i in range(2, question):
        if question % i == 0:
            return False
    return True


def function():
    question = randint(0, 100)
    if function_1(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
