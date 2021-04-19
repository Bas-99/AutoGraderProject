# ----------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------MultipleAssignmentExecuter.py-----------------------------------------------#
# ----------------------------------------------------------------------------------------------------------------------#
# This is the main file. When executing this file all relevant files and functions will be called to collect the       #
# simulation data for grading the assignments. In this file the frame rate for the screen recorder can be set          #
# ----------------------------------------------------------------------------------------------------------------------#

import cv2
import time
import os.path
from TestExecuter import testExecuter
from DirectoryManager import FolderAdder, path2_dh_DT, getAssignments, ScratchFolder
from DirectoryInitializer import StudentAssignmentFolder, test_names, general_path, path_unity, path_TwinCat, \
    MlModelFolder
from GraderAndTextEditor import autoGrader

# please make sure before running this, that TwinCat does NOT require
# you to fill in a verification code. Please check this beforehand.
if not general_path is None:
    if not path_unity is None:
        if not path_TwinCat is None:
            dir_assignments = StudentAssignmentFolder()
            dir_model = MlModelFolder(test_names)
            if not len(os.listdir(dir_assignments)) == 0:
                if not len(os.listdir(os.path.join(dir_model, test_names[0]))) == 0:
                    # defining frame rate
                    fps = 10.0

                    # defining the codec
                    fourcc_avi = cv2.VideoWriter_fourcc(*"XVID")

                    # the function ScratchFolder() will add a sub-directory named "scratch_videos" to
                    # the general path. In this folder the scratch videos will be stored.
                    ScratchFolder()

                    # the function FolderAdder() will add a folder named "all_assignments_simulations"
                    # in which the simulation files of the tested models will be stored.
                    dir_simulations = FolderAdder(test_names)

                    dir_assignments = StudentAssignmentFolder()
                    assignments = getAssignments()

                    total_start = time.time()

                    # looping over all assignments
                    for i in range(len(assignments)):
                        as_start = time.time()
                        folder_dh_DT = os.path.join(dir_assignments, assignments[i], path2_dh_DT)
                        # running the testExecuter() function for every assignment
                        testExecuter(dir_simulations, fps, fourcc_avi, folder_dh_DT, assignments[i])
                        as_end = time.time()
                        as_duration = as_end - as_start
                        print("Performing all tests on " + assignments[i] + " took: " + str(as_duration) + " seconds")

                    total_end = time.time()
                    total_duration = total_end - total_start
                    print("All assingments were analyzed in: " + str(total_duration / 60) + " minutes")

                    # calling the autoGrader() function to grade all the given simulations
                    autoGrader()
                else:
                    str_dir_models = "CAUTION: models have not correctly been uploaded.\n" \
                                     "make sure to upload models to ml_models"
                    print(str_dir_models)
            else:
                str_dir_not_filled = "CAUTION: assignments have not correctly been uploaded.\n" \
                                     "make sure to upload assignments to all_assignments"
                print(str_dir_not_filled)
        else:
            str_twincat_not = "CAUTION: the following directory is not yet defined: path_TwinCat"
    else:
        str_unity_not = "CAUTION: the following directory is not yet defined: path_unity"
        print(str_unity_not)
else:
    str_caution = "CAUTION: the following directory " \
                  "is not yet defined: general_path"
    print(str_caution)
