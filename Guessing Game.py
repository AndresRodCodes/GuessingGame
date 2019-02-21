import random

firstNumOfRange = 1
lastNumOfRange = 10

random_num = random.randint(firstNumOfRange, lastNumOfRange)
numOfGuesses = 3

menu = 'Guessing Game\n' + \
       'The number to guess is between ' + str(firstNumOfRange) + ' and ' + str(lastNumOfRange) + \
       '\nYou have ' + str(numOfGuesses) + ' tries to guess the number\n'

print(menu)

while numOfGuesses > 0:

    user_guess = int(input('Enter a number from 1 to 10: '))

    if user_guess == random_num:
        print('Correct!', 'Your guess was', user_guess)
        print('You get a cookie.')
        break

    else:
        numOfGuesses -= 1

        if numOfGuesses > 0:
            print('Incorrect.', 'You entered', user_guess)
            print('You have', numOfGuesses, 'tries left')

        else:
            print('Game Over.', 'You entered', user_guess)
            print('The number to guess was', random_num)