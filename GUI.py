import tkinter as tk
from DirectoryInitializer import StudentAssignmentFolder, MlModelFolder, test_names

def GUIfunction():
    StudentAssignmentFolder()
    MlModelFolder(test_names)

def buttonGeneralClicked():
    label_general.configure(text="Directory submitted!")
    label_unity.configure(text="Directory submitted!")
    label_TwinCat.configure(text="Directory submitted!")

window = tk.Tk()
window.title("autoGrader")

# splitting the screen
window.columnconfigure([0],minsize=20)
window.rowconfigure([0,1,2,3,4,5],minsize=20)

label_general = tk.Label(text="Give general path:")
label_unity = tk.Label(text="Give the path of unity:")
label_TwinCat = tk.Label(text="Give the path of TwinCat:")
label_run_initializer = tk.Label(text="Run the functions to initialize folders")

button_run = tk.Button(text="Run folder initializer",width=20,command=GUIfunction)
button_submit = tk.Button(text="Submit the paths",width=20,command=buttonGeneralClicked)

label_run_initializer.grid(row=0,column=0,sticky='w',padx=5,pady=5)
button_run.grid(row=1,column=0,sticky='w',padx=5,pady=5)
label_general.grid(row=2,column=0,sticky='w',padx=5,pady=5)
label_unity.grid(row=3,column=0,sticky='w',padx=5,pady=5)
label_TwinCat.grid(row=4,column=0,sticky='w',padx=5,pady=5)
button_submit.grid(row=5,column=0,sticky='w',padx=5,pady=5)

window.mainloop()


