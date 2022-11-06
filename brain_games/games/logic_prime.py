from random import randint

condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def function_1():
    question = randint(1, 100)
    for i in range(2, question):
        if question % i == 0:
            return False
    return True

def function():
    if function_1():
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer

