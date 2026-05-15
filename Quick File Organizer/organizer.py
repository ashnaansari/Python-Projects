import os
import shutil

# folder path
folder = r'C:\Users\hp\Desktop\Project\Python Project\Quick File Organizer\test folders'

# Read all files in folder
files = os.listdir(folder)

for file in files :
    path = os.path.join(folder, file)

    if file.endswith(('.jpg', '.jpeg', '.png')):
        new_folder = os.path.join(folder, 'Images')
    elif file.endswith(".pdf"): 
        new_folder = os.path.join(folder, "PDFs") 
    elif file.endswith(".mp3"): 
        new_folder = os.path.join(folder, "Music") 
    else: 
        new_folder = os.path.join(folder, "Others")
    
    os.makedirs(new_folder, exist_ok=True)
    shutil.move(path,new_folder)
    print(file,"moved")