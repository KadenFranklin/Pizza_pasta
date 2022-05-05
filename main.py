import os
import json
import lzma
import shutil
import argparse
import cv2 as cv

# Timeline:
# by 4/22
# want to extract the amount of likes, comments and such from each post.
# want to have dataset sorted into pasta /pizza /people
# want to have some sort of working facial detection program using haarcascade
# work on code that will generate new xml files as presets

# by 4/29
# want to have a working version of haar-cascade training algorithm or whatever
# start creating individual modules that detect a specific ingredient

# These were attainable goals, but I simply got preoccupied with other things

# If I get everything else working I will work on not_comment again.
# dect_face - Checks if an img contains a face and moves it to the People directory
# get_face_count - Goes through People directory and tries to detect the same face multiple times
#                   (Want this to return some count of people, or x most common faces)
# make_pizza(s) - generates the xml file for preset of name 's'
# pizza_pie -

# To initialize the dataset must use a Library called instaloader.
# It did not work on my machine, but here is the code to replicate an instagram dataset.

# import instaloader
# L = instaloader.Instaloader()
# 	for post in Post.from_username(L.context, ‘eric_thepizzaguy’).get_posts():
# 		L.download_post(post, target = ‘#assets’)


def pizza_pie():
    x = 1
    # I will make this some helper function for make_pizza()
    # (idk what yet but I'll prob need to just space it out)
    # to detect different ingredients in an image, if the image is a slice of pizza


def make_pizza(s):
    # This will make a corresponding subdirectory in pizza, and then generate the xml file.
    # https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html
    new_path = path + s


def dect_face():
    # I had to use multiple cascade classifiers to check each image. I was getting a good number of false positives.

    face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    alt = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
    alt2 = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    alttre = cv.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')

    for file in os.listdir(path):
        if file.endswith('.jpg'):
            n_path = path + '\\' + file
            img = cv.imread(n_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray = cv.equalizeHist(gray)
            faces = face.detectMultiScale(gray, 1.1, 4)

            if faces is not None:
                for (x, y, w, h) in faces:
                    faceROI = gray[y:y+h, x:x+w]
                    eyes = eye.detectMultiScale(faceROI, 1.1)
                    alts = alt.detectMultiScale(gray, 1.1)
                    alts2 = alt2.detectMultiScale(gray, 1.1)
                    altstre = alttre.detectMultiScale(gray, 1.1)
                    print(f"File: {file} \n face:{len(faces)} \n eye:{eyes} \n alt1:{alts} \n alt2:{alts2} \n alt3:{altstre} \n ")
                    cv.imshow("Image", img)
                    cv.waitKey(1)
                    # An image most likely contains a face if the following classifiers are not none:
                    # frontal_face and eye_tree_eyeglass
                    # frontal_face and alt1, alt2, alt3
                    if len(faces) > 1 and len(eyes) >= 1:
                        shutil.copyfile(n_path, person + '\\' + file)
                        print(f"con. 1 copied {file} file. \n")
                    elif len(faces) >= 1 and (len(alts) >= 1 and len(alts2) >= 1 and len(altstre) >= 1):
                        shutil.copyfile(n_path, person + '\\' + file)
                        print(f"con. 2 copied {file} file. \n")



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


# Main Algorithm
# Uses code above to loop through images in pizza and person directories.
# Will attempt to create a frequency count of specific person.
# checks each image against presets - stores values in a dict where key is filename of img(date), and value is list
# of ingredients I might have to loop through the files to create these but list_of_piz = []
# (a list of lists(lists are pizza ingredients))
# "C:\Users\Kaden's Laptop\Downloads\assets"
path = r"C:\Users\Kaden's Laptop\Desktop\assets"
pizza = r"C:\Users\Kaden's Laptop\Desktop\assets\Pizza"
pasta = r"C:\Users\Kaden's Laptop\Desktop\assets\Pasta"
person = r"C:\Users\Kaden's Laptop\Desktop\assets\Person"
dect_face()

# pers_list = []
#       for peep in person:
#           if person not in list,
#               append to list
#           else:
#               make a new entry in list_of_per
#
#       find person with the highest count, maybe incorporate likes into calc somewhere
#           can also do sentiment analysis on posts including people ig
#           also do something with most liked post of a person

#       for pizz in pizza:
#
#
#       should make a frequency chart of ingredients over time
#           use the filenames in some way so that they are displayed
#           properly in chronological order
#
# To create a preset you must create a file beforehand to store the trained cascade classifier
# Then run make_pizza(s) where s is the file path of images you want to use as positive samples
# In my case I made.
#   'Pepperoni'
#   'Sausage'
#   'Mushroom'
#   'Ham'
#   'Tomato'
#   'Olive'
#   'Bacon'
#   'Pickle'
#   'Chicken'
#   'Onion'
#   'Jalapeño'
