import random
guess = int(input('Please enter an integer between 1 and 10: '))
random = random.randint(0, 11)
if guess == random:
    import random
    print('correct')

else:
    print('wrong')
    guess2 = int(input('Again: '))
    if guess2 == random:
        print('correct')
    else:
        print('wrong')
        guess3 = int(input('Last time: '))
        if guess3 == random:
            print('correct')
        else:
            print('wrong')






