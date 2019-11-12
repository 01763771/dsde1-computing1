def number_guessing_game():
    '''Number guessing game.'''
    import random
    input_1 = int(input('Guess a number between 1 and 10: '))
    random_1 = random.randint(1, 10)
    while input_1 != random_1:
        import random
        print('False')
        input_1 = int(input('Guess a number between 1 and 10: '))
        random_1 = random.randint(1, 10)
    print('True')