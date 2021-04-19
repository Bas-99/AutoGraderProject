#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------DirectoryManager.py-------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# This file contains everything about the directory and path files, which are required within this grading tool. Before#
# starting the grading process one should make sure that this file is correctly setup.                                 #
#----------------------------------------------------------------------------------------------------------------------#

import os
from DirectoryInitializer import general_path

#----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Directory-Filtered-Videos--------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#

# directory for the filtered videos (choose in if placed in correct or incorrect directory)

#----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Directories-App-Runner-----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#

# path for the simulation file, CAUTION: make sure to adjust this path to the right path
# folder_dh_DT = 'C:\\Users\\20182615\Documents\\Jaar 3\\BEP\\OldProjects\\FESTO112\\cif_plc_control'

# this path has to be changed to the path where all assignments are stored
path2_dh_DT = 'cif_plc_control'

# making a folder to store the scracht video files into
def ScratchFolder():
    dir_scratch = os.path.join(general_path,"scratch_videos")
    if not os.path.exists(dir_scratch):
        os.makedirs(dir_scratch)
    return dir_scratch

# run this function to get all group numbers of the uploaded assignments
def getAssignments():
    assignments = os.listdir(os.path.join(general_path,"all_assignments"))
    return assignments

def FolderAdder(test_names):
    dir_simulations = os.path.join(general_path,"all_assignment_simulations")
    if not os.path.exists(dir_simulations):
        os.makedirs(dir_simulations)
    for test in test_names:
        test_dir = os.path.join(dir_simulations,test)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)
    return dir_simulations

def scratchVidNames(test_names):
    names = []
    dir_scratch = ScratchFolder()
    for test in test_names:
        names.append(os.path.join(dir_scratch, test + ".avi"))
    return names

# model_path = "C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\grading\\models"



