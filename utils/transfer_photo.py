import os
import fnmatch
from typing import Final, final
import shutil

def transfer(initialPath,finalPath):
    
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
                    
                   
                    shutil.move(currfile,os.path.join(destpath,file))
                    print("done")

    return filename

