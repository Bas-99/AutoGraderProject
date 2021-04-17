# https://www.tensorflow.org/install/gpu
from tensorflow.keras.models import load_model
from Video2Frames import create_data
import numpy as np
import os

model_path = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\grading\\models'
simulation_path = "C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\grading\\simulations"
test_names = ["test1a","test1b","test2","test3a","test3b"]
grade_file_path = "C:\\Users\\20182615\\PycharmProjects\\SimulationRecorder_and_Filter\\sub_grades.txt"
seq_len = [250,350,350,350,350]

def last3(s):
    return s[-7:-4]

def gradingData():
    global name
    classes = ["correct","incorrect"]
    open(grade_file_path, 'w').close()
    print("grading file is cleaned")
    for name in test_names:
        test_path = os.path.join(simulation_path, name)
        file_path = os.path.join(model_path, name)
        new_model = load_model(file_path, compile=True)

        X = create_data(test_path,seq_len[test_names.index(name)])
        count = 0
        for x in X:
            score = 0
            samples_to_predict = []
            samples_to_predict.append(x)

            samples_to_predict = np.array(samples_to_predict)
            # print(samples_to_predict.shape)

            predictions = new_model.predict(samples_to_predict)

            classif = np.argmax(predictions, axis=1)

            files = []
            for file in os.listdir(test_path):
                if file.endswith(".avi"):
                    files.append(file)

            if classes[classif[0]] == "correct":
                score += 1
            string_grade = "Group " + last3(files[count]) + " scored " + str(score) + " point for " + name
            # print(string_grade)
            count += 1

            with open(grade_file_path, 'a') as the_file:
                the_file.write('{}\n'.format(string_grade))

        print("Test " + name + " is finished grading")

gradingData()




