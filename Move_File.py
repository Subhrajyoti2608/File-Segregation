import os
import shutil

from_dir="C:/Users/subhr/OneDrive/Documents/Downloaded_Files/Image_Files"
to_dir="C:/Users/subhr/OneDrive/Documents/Downloaded_Files"

listOfFiles=os.listdir(from_dir)
print(listOfFiles)
for files in listOfFiles:
    name,ext=os.path.splitext(files)
    #print(name)
    #print(ext)
    if(ext==""):
        continue
    if(ext in [".txt", ".pdf", ".doc", ".docx"]):

        path1 = from_dir+"/"+files
        path2 = to_dir+"/"+"Document_Files"
        path3 = to_dir+"/"+"Document_Files"+"/"+files
        print("path1",path1)
        print("path3",path3)

        if(os.path.exists(path2)):
            print("moving"+files+".......")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving"+files+".......")
            shutil.move(path1,path3)
