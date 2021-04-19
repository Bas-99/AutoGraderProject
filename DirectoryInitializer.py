#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------DirectoryInitializer.py---------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# This file contains the directory setup, which has to be changed to the user. First a general path has to be specified#
# Then a path for the unity simulation and TwinCat program have to be specified. Then this file can be ran, after it   #
# successfully ran, one should add the ML models to "ml_models" and the assignments to "all_assignments"               #
#----------------------------------------------------------------------------------------------------------------------#

import os

# making a folder to un-zip and store all the assignments into
def StudentAssignmentFolder():
    dir_assignments = os.path.join(general_path,"all_assignments")
    if not os.path.exists(dir_assignments):
        os.makedirs(dir_assignments)
    print("all_assignments folder has been added")
    return dir_assignments

# making folder with sub-directories to store the ML models into
def MlModelFolder(test_names):
    dir_models = os.path.join(general_path,"ml_models")
    if not os.path.exists(dir_models):
        os.makedirs(dir_models)
    for test in test_names:
        test_model_dir = os.path.join(dir_models,test)
        if not os.path.exists(test_model_dir):
            os.makedirs(test_model_dir)
    print("ml_models folder has been added")
    return dir_models

# first choose a general path to which the programm may add folders to save all models and videos
# SELECT GENERAL DIRECTORY HERE:
general_path = "C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\AutoGraderDir"

# choose the path on which the unity simulation has been saved
# SELECT UNITY DIRECTORY HERE:
path_unity = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\OldProjects\\FESTO112\\Digital Twin Program'

# choose the path on which TwinCat is installed
# SELECT TWINCAT DIRECTORY HERE:
path_TwinCat = 'C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\IDE'

test_names = ["test1a", "test1b", "test2", "test3a","test3b"]

# now the program will initialize some folders in the general directory selected above.

# first the function StudentAssignmentFolder() is ran, this will add a sub-directory
# named "all_assignments" to the general path that has been selected. Please after
# running this function un-zip the student assignments in this directory!
StudentAssignmentFolder()
str_note_assignments = "Please make sure to un-zip the to-be graded assignments inside the all_assignments directory."
print(str_note_assignments)

# this function will add a sub-directory to to the general path named "ml_models",
# to this folder, the already trained ML models will have to be saved. Please
# after running this function add the trained ML models in this directory.
MlModelFolder(test_names)
str_note_models = "Please make sure to save the trained ML models inside the ml_models directory."
print(str_note_models)

# after running DirectoryInitializer.py, the file MultipleAssignmentExecuter.py may
# be ran to retrieve the grades of the uploaded assignments.

