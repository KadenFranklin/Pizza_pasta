import os
import json
import lzma

# "C:\Users\Kaden's Laptop\Downloads\assets"
path = r"C:\Users\Kaden's Laptop\Desktop\assets"


# Timeline:
# by 4/22
# want to extract the amount of likes, comments and such from each post.

# want to have dataset sorted into people/ food items/ pizza
# want to have some sort of working facial detection program using haarcascade
# work on code that will generate new xml files as presets

# by 4/29
# want to have a working version of haar-cascade training algorithm or whatever
# start creating individual modules that detect a specific ingredient

# by 5/6
# hopefully all code works long before the time I have to present,
# and I will have plenty of time to analyse my data
# and everything will be okay.

# A main algorithm that will look something like this

#       I might have to loop through the files to create these but
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


def pizza_pie():
    deez = 0
    # to detect different ingredients in an image, if the image is a slice of pizza


def dect_face():
    deez = 1
    # want to have some sort of working facial detection program using haarcascade
    # https://www.youtube.com/watch?v=LopYA64KmdE

    # for every image in directory
    #   if face
    #   move to subdirectory


def not_comment():
    # this was originally meant to pull comments from the posts,
    # json files did not contain comments, but do contain likes,
    # and alt image text which I think will be funny to do sentiment analysis on

    count = 0
    for file in os.listdir(path):
        if file.endswith('.xz'):
            new_file = file
            new_file = new_file[:-8]
            new_file = new_file + '.txt'
            print(new_file)
            count += 1
            f = lzma.open(path + '\\' + file)
            json_bytes = f.read()
            stri = json_bytes.decode('utf-8')
            data = json.loads(stri)
            for x in data.values():
                print(x)
                count_2 = 1
                for y in x.keys():
                    another_count = 0
                    print(f"Element #: {count_2}")
                    print(y)

                    # rn this part is not working as intended, loops through
                    # every post, then does the first write for some reason

                    while y == 'accessibility_caption':
                        another_count += 1
                        for y2 in x.values():
                            print(f"{another_count}: {y2}")
                            if y2 is None:
                                break
                            if (another_count == count_2) & (y2 is str):
                                with open(new_file, "a") as f:
                                    f.write("\n")
                                    f.write(y2)
                                    print('successfully performed a write... my code works?!?!?!')
                                    break

                    while y == 'edge_liked_by':
                        another_count += 1
                        for y2 in x.values():
                            print(f"{another_count}: {y2}")
                            if y2 is None:
                                break
                            if (another_count == count_2) & (y2 is str):
                                with open(new_file, "a") as f:
                                    f.write("\n")
                                    f.write(y2)
                                    print('successfully performed a write... my code works?!?!?!')
                                    break

                    count_2 += 1
