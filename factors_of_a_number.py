n = int(raw_input('Input a number to be factored: '))


def factor(n):
    factors = [1, n]
    for i in range(2, (n/2)+1):
        if n % i == 0:
            factors.append(i)
    factors = sorted(factors)
    print factors

factor(n)

"""
GOAL
Define a function that creates a list of all the numbers that are factors of the user's number. For example, if the
function is called factor, factor(36) should return [1,2,3,4,6,9,12,18,36]. The numbers in your list should be from
least to greatest, and 1 and the original number should be included.
"""

__author__ = 'scullinan'
