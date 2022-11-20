from random import randint

CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question < 2:
        return False
    for i in range(2, question):
        if question % i == 0:
            return False
    return True


def logic_game():
    question = randint(0, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
