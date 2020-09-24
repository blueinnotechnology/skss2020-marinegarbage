import glob
import os
import sys

# import Tkinter
# import Tkconstants
# import tkFileDialog
# while True:
#     print("Please select your image directory.")
#     current_dir = tkFileDialog.askdirectory()
#     if current_dir == None or current_dir == "":
#         print("You must select a directory.")
#         continue
#     break
# current_dir = os.getcwd()+"/darknet/train_data/coke"
# base_url = os.getcwd() + "/"
# current_dir = base_url + sys.argv[1]
current_dir = sys.argv[1] + "/"
base_url = current_dir + "../"
print("Base Directory: {}".format(base_url))
print("Photo Directory: {}".format(current_dir))

# Percentage of images to be used for the test set
percentage_test = 10
# Create and/or truncate train.txt and test.txt
file_train = open(base_url + 'train.txt', 'w')
file_test = open(base_url + 'test.txt', 'w')
# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1

for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.png")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.png' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.png' + "\n")
        counter = counter + 1