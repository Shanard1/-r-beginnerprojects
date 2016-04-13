ChangeCalculator = 1
coins = []


class Coin(object):

    def __init__(self, value, count, plural):
        self.value = value
        self.count = count
        self.plural = plural
        coins.append(self)

    amount = 0

penny = Coin(.01, 0, 'pennies')
nickel = Coin(.05, 0, 'nickels')
dime = Coin(.1, 0, 'dime')
quarter = Coin(.25, 0, 'quarters')

while ChangeCalculator == 1:
    CalculateChange = raw_input('Would you like to calculate some change? [Y/N]: ')
    if CalculateChange == 'y':
        ChangeInput = raw_input('Enter your amount of change: ')
        ChangeInput = float(ChangeInput)
        for c in coins:
            c.amount = int(ChangeInput/c.value)
            ChangeInput = ChangeInput%c.value
            print('You will need %d %s, %d %s, %d %s, and %d %s' % (coins[0].amount, coins[0].plural,
                                                                    coins[1].amount, coins[1].plural,
                                                                    coins[2].amount, coins[2].plural,
                                                                    coins[3].amount, coins[3].plural))
    elif CalculateChange == 'n':
        print 'Goodbye!'
        ChangeCalculator = 0
    else:
        print 'Sorry, I don\'t understand. Please try again!'






#q = int(1.47/.25)
#print q

'''
BASIC GOAL Imagine that your friend is a cashier, but has a hard time counting back change to customers. Create a
program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and
pennies are needed to make up the amount needed.

For example, if he inputs 1.47, the program will tell that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

SUBGOALS
So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to
him and the price of the item. The program should then tell him the amount of each coin he needs like usual.

To make the program even easier to use, loop the program back to the top so your friend can continue to use the program
without having to close and open it every time he needs to count change.
'''

__author__ = 'scullinan'