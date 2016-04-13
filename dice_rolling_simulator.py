__author__ = 'scullinan'

import random

sides = int(raw_input('Input a number of sides: '))
times = int(raw_input('Input a number of times rolled: '))

results = []
results_values = []

for x in range(0,times):
    n = random.randint(1,sides)
    results.append(n)

results = sorted(results)

for x in results:
    if x not in results_values:
        results_values.append(x)

print results
print results_values

for x in results_values:
    # print 'Result: x | Frequency: x', where Frequency = results_values.count(x)
    print 'Result: %d | Frequency %d' % (x, results.count(x))

'''
Goal
By using the random module, python can do things like pseudo-random number generation. So in this program, allow the
user to input the amount of sides on a dice and how many times it should be rolled. From there, your program should
simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed). After
that, print out how many times each number came up.
Subgoal
Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting
them to type in a real number until they do so.
Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire
program.
In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can,
round the percentage to 4 digits total OR two decimal places.
'''