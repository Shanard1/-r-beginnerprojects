__author__ = 'scullinan'

import random

goal = int(random.randrange(1,100,1))

print goal
guess_num = 0
game = True

while game == True:
    guess = int(raw_input('Enter a guess: '))
    guess_num = guess_num + 1

    if guess < goal:
        print 'Guess is less than the goal.'

    if guess > goal:
        print 'Guess is greater than the goal.'

    if guess == goal:
        print 'Congratulations! You win!'
        print 'You required %d guesses.' % guess_num

print 'Congratulations! You win!'
print 'You required %d guesses.' % guess_num



'''
BASIC GOAL Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to
guess what the number is. After every guess, the computer should tell the user if the guess is higher or lower than the
answer. When the user guesses the correct number, print out a congratulatory message.

SUB GOALS
- Add an introduction message that explains to the user how to play your game.
- In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before
the user arrived at the correct answer.
- At the end of the game, allow the user to decide if they want to play again (without having to restart the program).
'''