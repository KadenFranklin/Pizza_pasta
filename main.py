import os
import json
import lzma
import argparse
import cv2 as cv

# To initialize the dataset must use a Library called instaloader.
# It did not work on my machine, but here is the code to replicate an instagram dataset.

# import instaloader
# L = instaloader.Instaloader()
# 	for post in Post.from_username(L.context, ‘eric_thepizzaguy’).get_posts():
# 		L.download_post(post, target = ‘#assets’)

# "C:\Users\Kaden's Laptop\Downloads\assets"
path = r"C:\Users\Kaden's Laptop\Desktop\assets"


# Timeline:
# by 4/22
# want to extract the amount of likes, comments and such from each post.
# want to have dataset sorted into pasta /pizza /people
# want to have some sort of working facial detection program using haarcascade
# work on code that will generate new xml files as presets

# by 4/29
# want to have a working version of haar-cascade training algorithm or whatever
# start creating individual modules that detect a specific ingredient

# (These were attainable goals, but I simply got preoccupied with other things)
# Moving forward:
# 1 Week Till presentation

# If I get everything else working I will work on not_comment again.
# dect_face - Checks if an img contains a face and moves it to the People directory
# get_face_count - Goes through People directory and tries to detect the same face multiple times
#                   (Want this to return some count of people, or x most common faces)
# make_pizza(s) - make s subdirectory in Pizza
# pizza_pie -

# Main Algorithm -

# will look something like this

#       I might have to loop through the files to create these but
#       list_of_piz = [] (a list of lists(lists are pizza ingredients))
#       list_of_per = [] (or maybe a dict) entries are (count, img/path )
#
#       for every file:
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
# To create a preset you must create a file beforehand to store the trained cascade classifier
# Then run make_pizza(s) where s is the file path of images you want to use as positive samples
# In my case I made.
#   Pepperoni
#   Sausage
#   Mushroom
#   Ham
#   Tomato
#   Olive
#   Bacon
#   Pickle
#   Chicken
#   Onion
#   Jalapeño
#   Macaroni - might give false positives


def pizza_pie():
    # i will make this some helper function for make_pizza()
    #(idk what yet but I'll prob need to just space it out)
    # to detect different ingredients in an image, if the image is a slice of pizza


def make_pizza(s):
    # This will make a corresponding subdirectory in pizza, and then generate the xml file.
    # https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html
    new_path = path + s


def dect_face():
    # https://www.youtube.com/watch?v=LopYA64KmdE
    face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    for file in os.listdir(path):
        if file.endswith('.jpg'):
            img = cv.imread(file)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = face.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h,) in faces:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            new_dir = r"C:\Users\Kaden's Laptop\Desktop\assets\person"


def not_comment():
    # this was originally meant to pull comments from the posts,
    # json files did not contain comments, but do contain likes,
    # and alt image text which I think will be funny to do sentiment analysis on
    count = 0
    for file in os.listdir(path):
        if file.endswith('.xz'):
            new_file = file[:-8]
            new_file = new_file + '.txt'
            f = lzma.open(path + '\\' + file)
            json_bytes = f.read()
            stri = json_bytes.decode('utf-8')
            data = json.loads(stri)
            count += 1
            print(f"File #:{count}, {new_file}")
            count_2 = 0
            for (x_key, x_val) in data.items():
                if x_val == 'accessibility_caption':
                    print("huh_what how")
                    break
                if x_val == 'edge_liked_by':
                    print("huh_what how")
                    break
                if x_val.items() is not None:
                    for (key, val) in (x_val.items()):
                        count_2 += 1
                        print(f"Element #: {count_2}, {key}: {val}")
                        if key == 'accessibility_caption':
                            if val is not None:
                                with open(new_file, "a") as f:
                                    f.write("\n")
                                    f.write(val)
                                    print('successfully performed a write... my code works?!?!?!')
                                    break

                        if key == 'edge_liked_by':
                            if val is not None:
                                with open(new_file, "a") as f:
                                    f.write("\n")
                                    print(val)
                                    f.write(val)
                                    print('successfully performed a write... my code works?!?!?!')
                                    break
