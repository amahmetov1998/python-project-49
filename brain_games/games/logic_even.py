from random import randint
random_number = randint(1, 100)

def logic_even5():
    if random_number % 2 == 0:
        return correct_answer == 'yes'
    elif random_number % 2 != 0:
        return correct_answer == 'no'
