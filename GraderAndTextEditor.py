#----------------------------------------------------------------------------------------------------------------------#
#------------------------------------------GraderAndTextEditor.py------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# In this file the captured simulation videos will be graded using the derived machine learning models. These grades   #
# are then neatly formatted into two files, one which contains the total grades for every group                        #
# ("final_grades.txt) and one which contains the total and sub grades for every group ("extended_final_grades.txt)     #
#----------------------------------------------------------------------------------------------------------------------#

# https://www.tensorflow.org/install/gpu

# relevant libraries and dependencies are imported
from tensorflow.keras.models import load_model
from Video2Frames import create_data
import numpy as np
import os
import time
from DirectoryManager import FolderAdder, gradeFolder
from DirectoryInitializer import test_names, MlModelFolder

# amount of frames is set for every test
# videos of first test contain 250 frames,
# videos of second test contain 350 frames etc.
seq_len = [250,350,350,350,350]
dir_simulations = FolderAdder(test_names)
dir_grades = gradeFolder()

# function to get the group number out of strings
def last3(s):
    return s[-7:-4]

# function to check if line is empty
def isLineEmpty(line):
    return len(line.strip()) == 0

# function to sort the files in ascending order
def fileSorter(filename):
    open("grades/result.txt", 'w').close()
    with open(filename, 'r') as f:
        lines = f.readlines()

    selected_lines = lines[:-1]
    selected_lines.sort()
    outF = open("grades/result.txt", 'w')
    for line in selected_lines:
        outF.write('{}\n'.format(line))
    outF.close()

# function to remove empty lines from the files
def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)

# function to remove duplicate lines in the files
def duplicateRemover(filename):
    lines_seen = set()  # holds lines already seen
    outfile = open("grades/result_cleaned.txt", "w")
    for line in open(filename, "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

# function to grade the assignments using the TensorFlow models,
# which are trained in Google Colab and downloaded on a local drive
# In this function, first first the data from the videos is converted to
# frames then these frame sequences are fed into the models to make a
# prediction. The log of these predictions are saved to "sub_grades.txt"
def gradingData():
    global name
    start = time.time()
    classes = ["correct","incorrect"]
    open("grades/sub_grades.txt", 'w').close()
    print("grading file is cleaned")
    dir_models = MlModelFolder(test_names)

    # looping over all different tests
    for name in test_names:
        start_test = time.time()
        test_path = os.path.join(dir_simulations, name)
        file_path = os.path.join(dir_models, name)

        # loading the ML model
        new_model = load_model(file_path, compile=True)

        # storing the data to X
        X = create_data(test_path,seq_len[test_names.index(name)])
        count = 0

        # looping over all different videos in the data array X
        for x in X:
            score = 0
            samples_to_predict = []
            samples_to_predict.append(x)

            samples_to_predict = np.array(samples_to_predict)

            # making a prediction using the ML model
            predictions = new_model.predict(samples_to_predict)

            classif = np.argmax(predictions, axis=1)

            # reading the group number from the file names
            files = []
            for file in os.listdir(test_path):
                if file.endswith(".avi"):
                    files.append(file)

            # rewarding score if the test has been completed correclty
            if classes[classif[0]] == "correct":
                score += 1

            string_grade = "Group " + last3(files[count]) + " scored " + str(score) + " point for " + name
            # print(string_grade)
            count += 1

            # write the strings with the grades to "sub_grades.txt"
            with open("grades/sub_grades.txt", 'a') as the_file:
                the_file.write('{}\n'.format(string_grade))

        end_test = time.time()
        duration_test = end_test - start_test

        # writing the duration per test to the file
        string_test = "Test {} finished grading in {} seconds".format(name, duration_test)
        with open("grades/sub_grades.txt", 'a') as the_file:
            the_file.write('{}\n'.format(string_test))
        print(string_test)

    end = time.time()
    duration = end - start

    # writing the duration of the total grading to the file
    duration_string = "Grading of all assignments took {} seconds".format(duration)
    print(duration_string)
    with open("grades/sub_grades.txt", 'a') as the_file:
        the_file.write('{}\n'.format(duration_string))

# This function goes over the points given by gradingData() and computes a total
# score per group. These scores are added to the files. The output of this
# function are two text files, one with the extended results:
# "extended_final_grades.txt" and one with short results: "final_grades.txt".
def finalGrade(filename):
    open("grades/final_grades.txt", 'w').close()
    open("grades/extended_final_grades.txt", 'w').close()
    new_lines = []
    final_grades = []

    n_line = 0
    points = 0

    # looping over every line in the file
    for line in open(filename, 'r'):
        new_lines.append(line)
        n_line += 1

        # testing if the score was 0 or 1, index 17 in
        # the string is where the score is put
        if line[17] == '1':
            points += 1

        # retrieving the group number from the lines
        group = line[6:9]

        # if statement, after every 5th line an extra line
        # is put with the total grade for that group.
        if n_line % len(test_names) == 0:
            grade = points
            string_final_grade = "The final grade of group {} is {} out " \
                                 "of {} points".format(group, grade, len(test_names))
            print(string_final_grade)
            new_lines.append(string_final_grade)
            final_grades.append(string_final_grade)
            points = 0

    # below the two text files are made and released
    outF = open("grades/final_grades.txt", 'w')
    outF2 = open("grades/extended_final_grades.txt", 'w')
    for line in final_grades:
        outF.write('{}\n'.format(line))
    outF.close()
    for line in new_lines:
        outF2.write('{}\n'.format(line))
    outF2.close()
    remove_empty_lines("grades/extended_final_grades.txt")

# this function is the one that should be called outside of this
# file. It will make sure the functions are called in the right
# order to get the grades.
def autoGrader():
    gradingData()
    fileSorter("grades/sub_grades.txt")
    remove_empty_lines("grades/result.txt")
    duplicateRemover("grades/result.txt")
    finalGrade("grades/result_cleaned.txt")








