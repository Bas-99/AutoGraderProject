#----------------------------------------------------------------------------------------------------------------------#
#------------------------------------------MultipleAssignmentExecuter.py-----------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# This is the main file. When executing this file all relevant files and functions will be called to collect the       #
# simulation data for grading the assignments. In this file the frame rate for the screen recorder can be set          #
#----------------------------------------------------------------------------------------------------------------------#

import cv2
import time
import os.path
from TestExecuter import testExecuter
from DirectoryManager import FolderAdder, path1_dh_DT,assignments, path2_dh_DT, filtered_video_per_assignment
from GraderAndTextEditor import autoGrader

# defining frame rate
fps = 10.0

# defining the codec
fourcc_avi = cv2.VideoWriter_fourcc(*"XVID")

FolderAdder()

total_start = time.time()

# looping over all assignments
for i in range(len(assignments)):
    as_start = time.time()
    folder_dh_DT = os.path.join(path1_dh_DT,assignments[i],path2_dh_DT)
    save_path_filtered = os.path.join(filtered_video_per_assignment, assignments[i])

    # running the testExecuter() function for every assignment
    testExecuter(save_path_filtered,fps,fourcc_avi,folder_dh_DT)
    as_end = time.time()
    as_duration = as_end - as_start
    print("Performing all tests on " + assignments[i] + " took: " + str(as_duration) + " seconds")

total_end = time.time()
total_duration = total_end - total_start
print("All assingments were analyzed in: " + str(total_duration/60) + " minutes")

# calling the autoGrader() function to grade all the given simulations
autoGrader()
