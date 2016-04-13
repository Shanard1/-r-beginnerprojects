__author__ = 'scullinan'

order = '5993348'
total = 0

items = [
    {'number':1, 'name':'Chicken Strips', 'price':3.50},
    {'number':2, 'name':'French Fries', 'price':2.50},
    {'number':3, 'name':'Hamburger', 'price':4.00},
    {'number':4, 'name':'Hotdog', 'price':3.50},
    {'number':5, 'name':'Large Drink', 'price':1.75},
    {'number':6, 'name':'Medium Drink', 'price':1.50},
    {'number':7, 'name':'Milk Shake', 'price':2.25},
    {'number':8, 'name':'Salad', 'price':3.75},
    {'number':9, 'name':'Small Drink', 'price':1.25}
]

order = [int(x) for x in order]

for x in order:
    if x == items[x-1]['number']:
        total = total + items[x-1]['price']

print total

'''
GOAL
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since
your restaurant only sells 9 different items, you assign each one to a number, as shown below.
Chicken Strips - $3.50
French Fries - $2.50
Hamburger - $4.00
Hotdog - $3.50
Large Drink - $1.75
Medium Drink - $1.50
Milk Shake - $2.25
Salad - $3.75
Small Drink - $1.25
To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate
the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are
ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the
program loops so the user can take multiple orders without having to restart the program each time.
SUBGOALS
If you decide to, print out the items and prices every time before the user types in an order.
Once the user has entered an order, print out how many of each item have been ordered, as well as the total price. If
an item was not ordered at all, then it should not show up.
'''
