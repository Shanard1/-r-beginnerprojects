import random

play = 1

response = [
    {'number': 1, 'fortune': 'It is certain'},
    {'number': 2, 'fortune': 'It is decidedly so'},
    {'number': 3, 'fortune': 'Without a doubt'},
    {'number': 4, 'fortune': 'Yes, definitely'},
    {'number': 5, 'fortune': 'You may rely on it'},
    {'number': 6, 'fortune': 'As I see it, yes'},
    {'number': 7, 'fortune': 'Most likely'},
    {'number': 8, 'fortune': 'Outlook good'},
    {'number': 9, 'fortune': 'Yes'},
    {'number': 10, 'fortune': 'Signs point to yes'},
    {'number': 11, 'fortune': 'Reply hazy try again'},
    {'number': 12, 'fortune': 'Ask again later'},
    {'number': 13, 'fortune': 'Better not tell you now'},
    {'number': 14, 'fortune': 'Cannot predict now'},
    {'number': 15, 'fortune': 'Concentrate and ask again'},
    {'number': 16, 'fortune': 'Don\'t count on it'},
    {'number': 17, 'fortune': 'My reply is no'},
    {'number': 18, 'fortune': 'My sources say no'},
    {'number': 19, 'fortune': 'Outlook not so good'},
    {'number': 20, 'fortune': 'Very doubtful'}
]

while play == 1:
    start_game = raw_input('Would you like to ask a question? [Y/N]: ')
    if start_game == 'y':
        question = raw_input('Ask me a question: ')
        answer = random.randint(0, 20)
        print response[answer]['fortune']
    elif start_game == 'n':
        print 'Goodbye!'
        play = 0
    else:
        print 'I don\'t understand.'

'''
Goal
I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it
gives an answer by way of a floating die with responses written on it. You can create one in python. You must:

1. Allow the user to enter their question
2. Display an in progress message( i.e. "thinking")
3. Create 20 responses, and show a random response
4. Allow the user to ask another question or quit
Bonus Using whatever module you like, add a gui. Your gui must have:
1. A box for users to enter the question
2. At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)
'''

__author__ = 'scullinan'
