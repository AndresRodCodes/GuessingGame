import random


class GuessingGame:

    def __init__(self):
        self.first_num_of_range = 1
        self.last_num_of_range = 10
        self.num_of_guesses = 3
        self.random_num = random.randint(self.first_num_of_range, self.last_num_of_range)

    def change_settings(self, fn, ln, ng):
        self.first_num_of_range = fn
        self.last_num_of_range = ln
        self.num_of_guesses = ng
        self.random_num = random.randint(self.first_num_of_range, self.last_num_of_range)

    def play_game(self):
        menu = 'Guessing Game\n' + \
               'The number to guess is between ' + \
               str(self.first_num_of_range) + ' and ' + str(self.last_num_of_range) + \
               '\nYou have ' + str(self.num_of_guesses) + ' tries to guess the number\n'

        print(menu)

        while self.num_of_guesses > 0:
            user_guess = int(input('Enter a number from %d to %d:' % (self.first_num_of_range, self.last_num_of_range)))

            if user_guess == self.random_num:
                print('Correct!', 'Your guess was', user_guess)
                print('You get a cookie.\n')
                break

            else:
                self.num_of_guesses -= 1

                if self.num_of_guesses > 0:
                    if self.num_of_guesses == 1:
                        print('Incorrect.', 'You entered', user_guess)
                        print('You have', self.num_of_guesses, 'try left\n')
                    else:
                        print('Incorrect.', 'You entered', user_guess)
                        print('You have', self.num_of_guesses, 'tries left\n')
                else:
                    print('Game Over.', 'You entered', user_guess)
                    print('The number to guess was', self.random_num, '\n')


play_again_string = 'Play Again? y-yes, cs-change settings, q-quit\n'
player1 = GuessingGame()
player1.play_game()

user_play_again = input(play_again_string)

if user_play_again == 'cs':
    start_num = int(input('Enter start number: \n'))
    last_num = int(input('Enter last number: \n'))
    number_guesses = int(input('Enter number of guesses: \n'))

    player1.change_settings(start_num, last_num, number_guesses)
    player1.play_game()
    user_play_again = (input(play_again_string))

    while user_play_again == 'y':
        player1.change_settings(start_num, last_num, number_guesses)
        player1.play_game()
        user_play_again = (input(play_again_string))


while user_play_again == 'y':
    player1.__init__()
    player1.play_game()
    user_play_again = input(play_again_string)

print('Thank you for playing!')
