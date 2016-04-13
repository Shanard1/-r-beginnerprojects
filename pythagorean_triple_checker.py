go = 1


def check_pythagorean(a, b, c):

    sides = sorted([a, b, c])
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a ** 2 + b ** 2 == c ** 2:
        print '%d + %d = %d' % (a**2, b**2, c**2)
        print 'True'
    else:
        print '%d + %d != %d' % (a**2, b**2, c**2)
        print 'False'

while go == 1:
    pythag_check = raw_input('Would you like to check for a Pythagorean Triple? [Y/N]: ')
    if pythag_check == 'y':
        a = int(raw_input('side a: '))
        b = int(raw_input('side b: '))
        c = int(raw_input('side c: '))
        check_pythagorean(a, b, c)
    elif pythag_check == 'n':
        print 'Goodbye!'
        go = 0
    else:
        print 'I\'m sorry. I don\'t understand that command.'

'''
BACKGROUND INFORMATION
If you do not know how basic right triangles work, read this article on wikipedia.

https://en.wikipedia.org/wiki/Pythagorean_triple


MAIN GOAL
Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a
Pythagorean Triple or not.

SUBGOALS
1. If your program requires users to input the sides in a specific order, change the coding so the user can type in the
sides in any order. Remember, the hypotenuse (c) is always the longest side.
2. Loop the program so the user can use it more than once without having to restart the program.
'''

__author__ = 'scullinan'
