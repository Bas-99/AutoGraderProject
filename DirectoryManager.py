#----------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------DirectoryManager.py-------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# This file contains everything about the directory and path files, which are required within this grading tool. Before#
# starting the grading process one should make sure that this file is correctly setup.                                 #
#----------------------------------------------------------------------------------------------------------------------#

import os

# directory for the scrap videos
video_name1 = "test1a.avi"
video_name2 = "test1b.avi"
video_name3 = "test2.avi"
video_name4 = "test3a.avi"
video_name5 = "test3b.avi"
save_path = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\scratch_video'
completeName1 = os.path.join(save_path,video_name1)
completeName2 = os.path.join(save_path,video_name2)
completeName3 = os.path.join(save_path,video_name3)
completeName4 = os.path.join(save_path,video_name4)
completeName5 = os.path.join(save_path,video_name5)
names = [completeName1, completeName2, completeName3, completeName4, completeName5]

#----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Directory-Filtered-Videos--------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#

# directory for the filtered videos (choose in if placed in correct or incorrect directory)
save_path_filtered = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\filtered_videos\\test1'
vid_names = ["test1a", "test1b", "test2", "test3a","test3b"]

#----------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Directories-App-Runner-----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#

# path for the unity application, CAUTION: make sure to adjust this path to the right path
path_unity = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\OldProjects\\FESTO112\\Digital Twin Program'

# path for the TwinCat application, CAUTION: make sure to adjust this path to the right path
path_TwinCat = 'C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\IDE'

# path for the simulation file, CAUTION: make sure to adjust this path to the right path
# folder_dh_DT = 'C:\\Users\\20182615\Documents\\Jaar 3\\BEP\\OldProjects\\FESTO112\\cif_plc_control'

# this path has to be changed to the path where all assignments are stored
path1_dh_DT = 'C:\\Users\\20182615\Documents\\Jaar 3\\BEP\\OldProjects'
# FESTO 101 defective
assignments = ["FESTO102","FESTO103","FESTO105","FESTO107","FESTO108",
               "FESTO109","FESTO110","FESTO111","FESTO113","FESTO114","FESTO115"]
path2_dh_DT = 'cif_plc_control'

filtered_video_per_assignment = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\filtered_videos\\test1'

def FolderAdder():
    for assignment in assignments:
        newpath = os.path.join(filtered_video_per_assignment,assignment)
        if not os.path.exists(newpath):
            os.makedirs(newpath)

# setting the path where the ML models are stored
model_path = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\grading\\models'

# setting the path where to retrieve the simulation videos
simulation_path = "C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\EncodingDecoding\\grading\\simulations"

