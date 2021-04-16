import os
import pyautogui
import time
import ctypes
import psutil

offset_h = 0
offset_v = 0

# path for the unity application, CAUTION: make sure to adjust this path to the right path
path_unity = 'C:\\Users\\20182615\\Documents\\Jaar 3\\BEP\\OldProjects\\FESTO112\\Digital Twin Program'

# path for the TwinCat application, CAUTION: make sure to adjust this path to the right path
path_TwinCat = 'C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\IDE'

# path for the simulation file, CAUTION: make sure to adjust this path to the right path
folder_dh_DT = 'C:\\Users\\20182615\Documents\\Jaar 3\\BEP\\OldProjects\\FESTO112\\cif_plc_control'

def appRunner(path_unity,path_TwinCat,folder_dh_DT):
    # definition of the required file names (standard names)
    unity_sim = 'Festo MPS Distributing and Handling.exe'
    dir_sim = os.path.join(path_unity, unity_sim)

    TwinCat = 'devenv.exe'
    dir_Twin = os.path.join(path_TwinCat, TwinCat)

    sim_folder = 'TwinCAT template Digital Twin'
    sim_file = 'dh_plc_DT.sln'

    file_dh_DT = 'dh_DT.xml'
    dir_dh_DT = os.path.join(folder_dh_DT, file_dh_DT)

    # the following line will open the TwinCat program
    if "devenv.exe" in (i.name() for i in psutil.process_iter()):
        print("TwinCat is already opened")
        # force it to close TwinCat?
    else:
        os.startfile(dir_Twin)
    time.sleep(2)

    # this part will make sure the window TwinCat window is maximized
    pyautogui.keyDown('alt')
    pyautogui.press(' ')
    pyautogui.press('x')
    pyautogui.keyUp('alt')

    # press the FILE button, top left (1920x1080), and open project/solution
    pyautogui.click(28,50)
    pyautogui.moveTo(28, 109, duration=0.2, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(465, 109, duration=0.4, tween=pyautogui.easeInOutQuad)
    pyautogui.click(465, 109)

    # search for the simulation file in the already opened file explorer
    pyautogui.write(sim_folder)
    pyautogui.press('enter')
    pyautogui.write(sim_file)
    pyautogui.press('enter')

    # navigating through the menu on the left to go to the CIF folder
    time.sleep(9)
    pyautogui.click(102,272)
    time.sleep(0.5)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(0.5)

    # on the CIF folder import the XML file
    pyautogui.keyDown('shift')
    pyautogui.press('f10')
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

    # now the right XML file is chosen and imported, all files will be replaced
    pyautogui.write(dir_dh_DT)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)

    # the runtime will be activated and restarted
    pyautogui.click(262,113)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(4)

    # the system will login on the corresponding port
    pyautogui.click(1004,113)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)

    # the unity simulation is started
    if "Festo MPS Distributing and Handling.exe" in (i.name() for i in psutil.process_iter()):
        print("Unity is already opened")
        # force it to close unity?
    else:
        os.startfile(dir_sim)
    time.sleep(2)

    # the system switches back to TwinCat to login into the simulation
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(2)
    pyautogui.click(1029,113)

    # the simulation window is reopened and maximized
    time.sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMISE = 3
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, SW_MAXIMISE)

    # the simulation is initialized in the following steps
    time.sleep(8)
    # filling the left stack
    pyautogui.click(360,507)
    # filling the middle stack
    pyautogui.click(400,507)
    # filling the right stack
    pyautogui.click(440,507)

    # switching to automatic mode
    pyautogui.mouseDown(318,488)
    time.sleep(2)
    pyautogui.mouseUp()

    # right-click the start button to start the simulation
    time.sleep(2)
    pyautogui.click(287,462,button='right')

    # # switching to manual mode
    # pyautogui.mouseDown(318,488,button='right')
    # time.sleep(2)
    # pyautogui.mouseUp(button='right')

    # # pressing the reset button
    # pyautogui.click(287,488)

    # # pressing the stop button
    # pyautogui.click(319,464)

start = time.time()

# calling the function
appRunner(path_unity,path_TwinCat,folder_dh_DT)

end = time.time()
duration = end - start
print("The simulation setup took: "+str(duration)+" seconds")