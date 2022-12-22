import os
import fnmatch
from typing import Final, final
import shutil

def transfer(initialPath,finalPath):
    #path = "C:/Users/RAMAN KUMAR/Downloads"
    #print(os.listdir(path))
    fileKeyWords="*#*.jpg"
    filename=[]

    for root,dir,files in os.walk(initialPath):
        for file in files:
                if fnmatch.fnmatch(file,fileKeyWords):
                    filename.append(file)
                    
                    currfile=os.path.join(root,file)
                    destpath=finalPath
                    if not os.path.isdir(destpath):
                        os.mkdir(destpath)
                    
                    # print(os.path.isdir(destpath))
                    # print(os.path.isfile(currfile))
                    #os.replace(currfile,os.path.join(destpath,file))
                    shutil.move(currfile,os.path.join(destpath,file))
                    print("done")

    return filename

