estimator_on = 1

coins = []
coin_sum = 0


class Coin(object):

    def __init__(self, plural, grams_weight, value, input_weight, count, wrapper):
        self.plural = plural
        self.grams_weight = grams_weight
        self.value = value
        self.input_weight = input_weight
        self.count = count
        self.wrapper = wrapper
        coins.append(self)


penny = Coin('pennies', 2.5, .01, 0, 0, 50)
nickel = Coin('nickels', 5, .05, 0, 0, 40)
dime = Coin('dimes', 2.268, .1, 0, 0, 50)
quarter = Coin('quarters', 5.67, .25, 0, 0, 40)


def coin_weight(coin):
    if g_or_p == 'g':
        coin.input_weight = float(raw_input('What is the weight of the %s in grams?: ' % coin.plural))
    elif g_or_p == 'p':
        coin.input_weight = float(raw_input('What is the weight of the %s in pounds?: ' % coin.plural))


def coin_count(coin):
    if g_or_p == 'g':
        coin.count = coin.input_weight / coin.grams_weight
    elif g_or_p == 'p':
        coin.count = (coin.input_weight * 453.592) / coin.grams_weight


def coin_wrap(coin):
    print ('You have %d wrapper(s) worth of %s' % (coin.count/coin.wrapper, coin.plural))

while estimator_on == 1:
    weigh_coins = raw_input('Would you like to weigh your coins? [Y/N]: ')
    if weigh_coins == 'y':
        g_or_p = raw_input('Would you like to submit your coins in grams (g) or pounds (p)? [G/P]: ')
        for c in coins:
            coin_weight(c)
        for c in coins:
            coin_count(c)
        for c in coins:
            coin_wrap(c)
        for c in coins:
            coin_sum += c.count*c.value

        print ('Your coin input is worth approximately %d dollars. Goodbye!' % coin_sum)
    elif weigh_coins == 'n':
        print 'Goodbye!'
        estimator_on = 0
    else:
        print 'I\'m sorry. I don\'t understand that command.'

'''
When some people receive change after shopping, they put it into a container and let it add up over time.
Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what
they are worth. While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you
will need. Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then
estimate how many of each type you have and then how many wrappers you'll need.

For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about
563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Goal Create a program that allows the user to input the total weight of each type of coin they have (pennies, nickels,
dimes, and quarters), and then print out how many of each type of wrapper they would need, how many coins they have,
and the estimated total value of all of their money.

Weight of each coin:
http://www.usmint.gov/about_the_mint/?action=coin_specifications
penny = 2.5g
nickel = 5.0g
dime = 2.268g
quarter = 5.67g

How many fit in each wrapper:
https://en.wikipedia.org/wiki/Coin_wrapper#Amount_in_a_roll_in_the_United_States
penny = 50
nickel = 40
dime = 50
quarter = 40

Subgoals
Round all numbers printed out to the nearest whole number.
Allow the user to select whether they want to submit the weight in either grams or pounds.

CHALLENGES:

1. Create four inputs, one for the total weight of each kind of coin
2. Return the total number of wrappers for each coin
    a. This will involve writing either four functions, or a function that branches off to four outputs
3. Return the total number of coins
4. Return the total value of all the submitted money

'''

__author__ = 'scullinan'
