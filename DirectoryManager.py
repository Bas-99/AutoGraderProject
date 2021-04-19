#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------DirectoryManager.py-------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# This file contains some general directory managing, note this file does not require any additional input or changing #
#----------------------------------------------------------------------------------------------------------------------#

import os
from DirectoryInitializer import general_path

# below, the generilized sub-directory of the plc file is listed
path2_dh_DT = 'cif_plc_control'

# making a folder to store the scratch video files into
def ScratchFolder():
    dir_scratch = os.path.join(general_path,"scratch_videos")
    if not os.path.exists(dir_scratch):
        os.makedirs(dir_scratch)
    return dir_scratch

# run this function to get all group numbers of the uploaded assignments
def getAssignments():
    assignments = os.listdir(os.path.join(general_path,"all_assignments"))
    return assignments

# function to add sub-directories to store the video files of the tested simulations into
def FolderAdder(test_names):
    dir_simulations = os.path.join(general_path,"all_assignment_simulations")
    if not os.path.exists(dir_simulations):
        os.makedirs(dir_simulations)
    for test in test_names:
        test_dir = os.path.join(dir_simulations,test)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
    return dir_simulations

# adding sub-directories for the different scratch videos of the different tests
def scratchVidNames(test_names):
    names = []
    dir_scratch = ScratchFolder()
    for test in test_names:
        names.append(os.path.join(dir_scratch, test + ".avi"))
    return names




