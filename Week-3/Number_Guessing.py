import random
guess = int(input('Please enter an integer between 1 and 10 '))
random = random.randint(0, 11)

while guess != random:
    import random
    print('False')
    guess = int(input('Please enter an integer between 1 and 10 '))
    random = random.randint(0, 11)

print('True')


