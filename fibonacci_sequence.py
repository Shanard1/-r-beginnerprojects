__author__ = 'scullinan'

import re

nth = raw_input('Which term of the Fibonacci sequence would you like find?: ')

def check_nth(nth):
    if not re.match("^[0-9.]*$",nth):
        print 'Error! Only numbers are allowed!'
        print 5/0

check_nth(nth)

nth = int(nth)

fibonacci = [0, 1]

def fibo_sequence(n):
    if n > 2:
        for x in range(2,n):
            fibonacci.append(int(fibonacci[x-1]+fibonacci[x-2]))
        print fibonacci[n-1]
    elif n <= 2:
        print fibonacci[n-1]
    else:
        print fibonacci[0]

fibo_sequence(nth)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''
BACKGROUND INFORMATION If you do not know about the Fibonacci Sequence, read the information on MathIsFun.com.
GOAL
Define a function that allows the user to find the value of the nth term in the sequence. To make sure you've written
your function correctly, test the first 10 numbers of the sequence. Remember, the 0th term is 0 and the first and
second term are both 1.
'''
