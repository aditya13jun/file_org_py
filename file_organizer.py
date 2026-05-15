import os
import shutil

path = r"D:/temp/"

file_name = os.listdir(path)

folder_names = ['log files', 'pdf files', "image files", "doc files"]

for loop in range(0,4):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".log" in file and not os.path.exists(path + "log files/" + file):
        shutil.move(path + file, path + "log files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".docx" in file and not os.path.exists(path + "doc files/" + file):
        shutil.move(path + file, path + "doc files/" + file)