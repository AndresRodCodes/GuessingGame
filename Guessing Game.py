import random

def play_game():
    first_num_of_range = 1
    last_num_of_range = 10

    random_num = random.randint(first_num_of_range, last_num_of_range)
    num_of_guesses = 3

    menu = 'Guessing Game\n' + \
           'The number to guess is between ' + str(first_num_of_range) + ' and ' + str(last_num_of_range) + \
           '\nYou have ' + str(num_of_guesses) + ' tries to guess the number\n'

    print(menu)

    while num_of_guesses > 0:

        user_guess = int(input('Enter a number from 1 to 10: '))

        if user_guess == random_num:
            print('Correct!', 'Your guess was', user_guess)
            print('You get a cookie.\n')
            break

        else:
            num_of_guesses -= 1

            if num_of_guesses > 0:
                print('Incorrect.', 'You entered', user_guess)
                print('You have', num_of_guesses, 'tries left\n')

            else:
                print('Game Over.', 'You entered', user_guess)
                print('The number to guess was', random_num, '\n')


play_game()

user_play_again = input('Play Again?\n')

while user_play_again == 'yes':
    play_game()
    user_play_again = input('Play Again?\n')
print('Thank you for playing!')
