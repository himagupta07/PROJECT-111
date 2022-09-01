import os
import shutil

from_dir= "C:/Users/Hp/Downloads"
to_dir= "C:/Users/Hp/Desktop"
list_of_files=os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,extension=os.path.splitext(files)
   # print(name)
   # print(extension)
    if extension==" ":
        continue
    if extension in ['.gif','.jpeg','.png','.jpg']:
        path1=from_dir+ '/' + files
        path2=from_dir+'/'+ "Image_files"
        path3= from_dir+'/'+ "Image_files"+'/'+files
        print("path1: ",path1)
        print("path3: ",path3)
        
        if os.path.exists(path2):
            print("moving...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("started moving...",path3)
            shutil.move(path1,path3)
