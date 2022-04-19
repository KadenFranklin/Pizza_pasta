

# want to extract the amount of likes, comments and such from each post.
# C:\Users\Kaden's Laptop\Desktop\#assets
# or
# C:\Users\Kaden's Laptop\Documents\GitHub\KadenFranklin.github.io\csci270\Pasta, Pizza, Person\#assets

# txt file contains that text associated with each post, already enough to do sentiment analysis on

# Timeline:
# by 4/22
# want to have dataset sorted into people/ food items/ pizza
# want to have comments in text file i think
# want to have some sort of working facial detection program using haarcascade
# work on code that will generate new xml files

# by 4/29
# want to have a working version of haar-cascade training algorithm or whatever
# start creating individual modules that detect a specific ingredient

# A main algorithm that will look something like this

#
#       list_of_piz = [] (a list of lists(lists are pizza ingredients))
#       list_of_per = [] (or maybe a dict) entries are (count, img/path )
#
#       for every picture:
#           -if person:
#              - if current person is similar enough to some other entry in list_of_per
#                   count += 1
#              - else:
#                   make a new entry in list_of_per
#           - if !person:
#              - if pizza
#                    check what kind of ingredients,
#                    store in list
#                    append to list_of_piz
#              - if !pizza
#                    not to be rude but kinda irrelevant
#
#       find person with the highest count, maybe incorporate likes
#       into calc somewhere
#           can also do sentiment analysis on posts including people ig
#           also do something with most liked post of a person
#
#       should make a frequency chart of ingredients over time
#           use the filenames in some way so that they are displayed
#           properly in chronological order
#
#       other ideas:
#


# by 5/6
# hopefully all code works long before the time I have to present,
# and I will have plenty of time to analyse my data
# and everything will be okay.

