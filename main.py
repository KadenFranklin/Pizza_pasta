import os
import json
import lzma
import shutil
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

# by 5/6
# all of my code will be working, with sufficient time to work through problems I encounter.

# These were attainable goals, but I simply got preoccupied with other things


def pizza_pie():
    # makes a text file directing to positive/negative samples as per:
    # https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html
    # I used the same negative images for each dataset, which is just images of people
    # You will have to move each pos.txt when running programs in cascadeutils.txt, these are specific to my project structure
    neg = r"C:\Users\kaden\Downloads\pizza_pasta\neg.txt"
    with open(neg, "a") as f:
        for x in os.listdir(person):
            f.write("Person/" + x + "\n")

    for y in os.listdir(pizza):
        new = pizza + "\\" + y + "\\" + "pos.txt"
        with open(new, "w") as f1:
            for yy in os.listdir(pizza + "\\" + y):
                if yy == "pos.txt":
                    break
                f1.write("\n")
                f1.write(yy)


def dect_face():
    # Checks if an img contains a face and moves it to the People directory
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
            faces = face.detectMultiScale(gray, 1.1, 8)
            if len(faces) >= 1:
                for (x, y, w, h) in faces:
                    faceROI = gray[y:y+h, x:x+w]
                    eyes = eye.detectMultiScale(faceROI, 1.1, 4)
                    alts = alt.detectMultiScale(gray, 1.1, 5)
                    alts2 = alt2.detectMultiScale(gray, 1.1, 5)
                    altstre = alttre.detectMultiScale(gray, 1.1, 5)
                    print(f"File: {file} \n face:{len(faces)} \n eye:{len(eyes)} \n alt1:{len(alts)} \n alt2:{len(alts2)} \n alt3:{len(altstre)} \n ")
                    # An image most likely contains a face if the following classifiers are not none:
                    # frontal_face and eye_tree_eyeglass
                    # frontal_face and alt1, alt2, alt3
                    if len(faces) >= 3:
                        shutil.copyfile(n_path, person + '\\' + file)
                        print(f"con. 1 copied {file} file. \n")
                    if len(faces) >= 1 and len(eyes) >= 1:
                        shutil.copyfile(n_path, person + '\\' + file)
                        print(f"con. 1/2 copied {file} file. \n")
                    elif len(faces) >= 2 and (len(alts) + len(alts2) + len(altstre)) >= 2:
                        shutil.copyfile(n_path, person + '\\' + file)
                        print(f"con. 2 copied {file} file. \n")
                    break


def not_comment():
    # this was originally meant to pull comments from the posts, json files did not contain comments, but do contain likes, and alt image text which I think will be funny to do sentiment analysis on
    # did not get this to work because of the layout of json files.
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


# def make_pizza(s):

# To initialize the dataset must use a Library called instaloader.
# It did not work on my machine, but here is the code to replicate an instagram dataset.

# import instaloader
# L = instaloader.Instaloader()
# 	for post in Post.from_username(L.context, ‘eric_thepizzaguy’).get_posts():
# 		L.download_post(post, target = ‘#assets’)

# Main Algorithm
# Calls above functions in appropriate locations, loops through person directory, and makes a frequency count per person
# Then loops through all images, checks each image against presets & stores values in a dict where key is filename of img(date), and value is list(of ingredients)
ocv = r"C:\Users\kaden\Downloads\opencv\build\x64\vc15\bin"
path = r"C:\Users\kaden\Downloads\assets"
pasta = r"C:\Users\kaden\Downloads\Pizza_pasta\Pasta"
pizza = r"C:\Users\kaden\Downloads\Pizza_pasta\Pizza"
person = r"C:\Users\kaden\Downloads\Pizza_pasta\Person"


# dect_face()
# pizza_pie()
# follow instructions in cascade utils.txt to create classifiers

jal = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Jalepeno\Data\cascade.xml"
mush = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Mushroom\Data\cascade.xml"
oli = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Olive\Data\cascade.xml"
oni = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Onion\Data\cascade.xml"
pep = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Pepperoni\Data\cascade.xml"
pic = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Pickle\Data\cascade.xml"
tom = r"C:\Users\kaden\Downloads\pizza_pasta\Pizza\Tomato\Data\cascade.xml"

# pers_list = []
# for peep in person:
#     x = 1
# what ability do we have to compare one face to another?
# if peep not in list,
#         append to list
#     else:
#         make a new entry in list_of_per

# for elem in pers_list
#   find highest count and display that image.

# ingredients = ['Pepperoni', 'Mushroom', 'Tomato', 'Olive', 'Pickle', 'Onion', 'Jalepeno']
#       for img in assets:
#
#       should make a frequency chart of ingredients over time
#           use the filenames in some way so that they are displayed
#           properly in chronological order
#

# sent_afinn = []
# for line in book_lines_list:
#     if afinn.score(line) > -50:
#         sent_afinn.append(afinn.score(line))
#
# sent_vader = []
# values_dict = {}
# for line in book_lines_list:
#     values = sid.polarity_scores(line)
#     values_dict[line] = values['compound']
#     if values['compound'] > -0.9999999:
#         sent_vader.append(values['compound'])

# def moving_average(data, window):
#     return [sum(data[i:i+window]) / window for i in range(len(data) - window)]
#
# book_window = 2**10
# n = moving_average(sent_afinn, book_window)
# plt.plot(range(len(n)), n)
# n = moving_average([s*5 for s in sent_vader], 2**10)
# plt.plot(range(len(n)), n)

