#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------TestExecuter.py---------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# This file executes the functions defined in TestFunctions.py one by one                                              #
#----------------------------------------------------------------------------------------------------------------------#

from TestFunctions import test_list
from TestFunctions import time_test1a, time_test1b, time_test2, time_test3a, time_test3b
from RecorderAndFilter import screenRec, frameFilter
from ProgramExecuter import appRunner, appCloser
from DirectoryManager import vid_names, names, path_unity, path_TwinCat,assignments

def testExecuter(save_path_filtered,fps,fourcc_avi,folder_dh_DT):

    # defining recording time
    sim_time = [time_test1a, time_test1b, time_test2, time_test3a, time_test3b]

    # video specifications
    widths = [124, 124, 204, 148, 96]
    heights = [138, 138, 46, 175, 122]

    sizes = [(widths[0],heights[0]),(widths[1],heights[1]),
             (widths[2],heights[2]),(widths[3],heights[3]),
             (widths[4],heights[4])]

    ofsets_h = [431, 431, 266, 1254, 1388]
    ofsets_v = [99, 99, 190, 232, 231]

    # setting the minimal area for detecting the moving object, higher means less noise
    factor = 0.2
    min_areas = [widths[0]*heights[0]*factor, widths[1]*heights[1]*factor,
                 widths[2]*heights[2]*factor, widths[3]*heights[3]*factor,
                 widths[4]*heights[4]*factor]

    threads = []
    count = 0
    for current_test in test_list:
        appRunner(path_unity, path_TwinCat, folder_dh_DT)

        current_test()

        screenRec(fps, sim_time[count], fourcc_avi, names[count],
                  widths[count], heights[count], sizes[count],
                  ofsets_h[count], ofsets_v[count])

        appCloser()
        frameFilter(names[count], min_areas[count], fps, heights[count],
                    widths[count], save_path_filtered, fourcc_avi, vid_names[count], assignments[count])
        count += 1