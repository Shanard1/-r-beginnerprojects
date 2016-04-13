__author__ = 'scullinan'

n_1 = raw_input('NOUN: ')
n_2 = raw_input('NOUN: ')
n_3 = raw_input('NOUN: ')
o_1 = raw_input('OCCUPATION: ')
v_1 = raw_input('VERB: ')
p_1 = raw_input('PLACE: ')
v_ed_1 = raw_input('VERB ENDING IN "ED": ')
n_4 = raw_input('NOUN: ')
v_ing_1 = raw_input('VERB ENDING IN "ING": ')
n_p_1 = raw_input('NOUN (PLURAL): ')
n_5 = raw_input('NOUN: ')
e_1 = raw_input('EMOTION: ')

story = '''It was during the battle of %s when I was running through a %s when a %s went off right next to
my platoon. Our %s yelled for us to %s to the nearest %s we could find. When we got to the
%s we %s to start a fire. As we were starting the fire the enemy saw the %s from the fire and
started %s %s at us. We all quickly ducked behind the %s at the %s and returned fire.
We quickly eliminated the enemy and were %s that we had won the battle.''' % (n_1, n_2, n_3, o_1, v_1, p_1, \
p_1, v_ed_1, n_4, v_ing_1, n_p_1, n_5, p_1, e_1)

print story




'''
Background
Ever played Mad Libs? If you haven't, here's the basic's of it.
"Mad Libs consist of a book that has a short story on each page with many key words replaced with blanks. Beneath each
blank is specified a lexical or other category, such as "noun", "verb", "place", or "part of the body".[10] One player
asks the other players, in turn, to contribute some word for the specified type for each blank, but without revealing
the context for that word. Finally, the completed story is read aloud. The result is usually comic, surreal and
somewhat nonsensical."
Goal
Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story
with the words that the user inputted. The story doesn't have to be too long, but it should have some sort of story
line.

Tip - It's easiest to write out a quick story on a piece of paper or a word document, and then go back through and see
which words the user should be able to change.

Subgoals
If the user has to put in a name, change the first letter to a capital letter.
Change the word "a" to "an" when the next word in the sentence begins with a vowel.

http://www.madglibs.com/showglib.php?glibid=181
'''