__author__ = 'scullinan'

for i in range(99, 0, -1):
    if i > 1:
        print ('%d bottles of beer on the wall,' % int(i))
        print ('%d bottles of beer,' % int(i))
        print ('you take one down and pass it around')
        print ('%d more bottles of beer on the wall' % (int(i)-1))
        print ('')
    else:
        print ('%d bottle of beer on the wall,' % int(i))
        print ('%d bottle of beer,' % int(i))
        print ('you take one down and pass it around \n'
               'no more bottles of beer on the wall')

'''
GOAL
Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty
simple program, so to make it a bit harder, here are some rules to follow.

RULES
1. If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in
function.
2. Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
3. Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
Put a blank line between each verse of the song.
'''