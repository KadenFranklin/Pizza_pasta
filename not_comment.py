import os
import json
import lzma
# this was originally meant to pull comments from the posts,
# json files did not contain comments, but do contain likes,
# and alt image text which I think will be funny to do sentiment analysis on

count = 0
path = r"C:\Users\Kaden's Laptop\Desktop\assets"
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




