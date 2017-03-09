# deprecated
##################

import os
import psutil
import shutil
import subprocess
import time

import win32com.client as com

from old_lib import util


def copy_sd2hd():

    MB = 1024 * 1024.0
    camera_path = os.path.abspath(util.config.get("Foldersettings", "camerapath"))
    archive_path = os.path.abspath(util.config.get("Foldersettings", "archivepath"))

    for folder in os.listdir(camera_path):
        src_path = os.path.abspath(camera_path + "\\" + folder)
        folderyear = time.gmtime(os.path.getmtime(src_path))[0]
        dest_path = os.path.abspath(archive_path + "\\" + str(folderyear) + "\\" + folder)
        fso = com.Dispatch("Scripting.FileSystemObject")
        srcfoldersize = (fso.GetFolder(src_path).Size / MB)
        destspace = psutil.disk_usage("F:\\_FOTOGRAFIE").free / MB

        print "---------------------------"
        print " Foldername:   %s" %folder
        print " Year:         %s" %folderyear
        print " Size:         %.2f MB" %srcfoldersize
        print " Copying from %s to %s" %(src_path, dest_path)

        if srcfoldersize > destspace:
            print " Not enough Space in Destination"
        elif os.path.exists(dest_path):
            print " Path already existing. Skipping ..."
        else:
            shutil.copytree(src_path, dest_path)
            print " Copy complete, opening Explorer"
            subprocess.Popen(r'explorer /select, "' + dest_path + '\\"')

        print "---------------------------"
        print " "


