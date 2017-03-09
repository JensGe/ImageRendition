import os, configparser, time, shutil, psutil, subprocess

import win32com.client as com


config = configparser.ConfigParser()
config.read_file(open('config.cfg'))

camera_path = os.path.abspath(config.get("Foldersettings", "camerapath"))
archive_path = os.path.abspath(config.get("Foldersettings", "archivepath"))

def listdirs(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]


def listemptyfolders(rootfolder):
    emptyfolders = []
    for yearfolder in os.listdir(rootfolder):
        for folder in os.listdir(rootfolder + "\\" + yearfolder):
            if listdirs(rootfolder + "\\" + yearfolder + "\\" + folder) == []:
                emptyfolders.append([yearfolder,folder])
    return emptyfolders


def createfolders(emptyfolder):
    emptyfolderpath = os.path.abspath(archive_path + "\\" + emptyfolder[0] + "\\" + emptyfolder[1])
    if not os.path.exists(emptyfolderpath + "\\RAW"):
        os.makedirs(emptyfolderpath + "\\RAW")
        print(emptyfolderpath + "\\RAW created.")
    if not os.path.exists(emptyfolderpath + "\\JPG-HQ"):
        os.makedirs(emptyfolderpath + "\\JPG-HQ")
        print(emptyfolderpath + "\\JPG-HQ created.")

def copy_sd2hd():

    MB = 1024 * 1024.0

    for folder in os.listdir(camera_path):
        src_path = os.path.abspath(camera_path + "\\" + folder)
        folderyear = time.gmtime(os.path.getmtime(src_path))[0]
        dest_path = os.path.abspath(archive_path + "\\" + str(folderyear) + "\\" + folder)
        fso = com.Dispatch("Scripting.FileSystemObject")
        srcfoldersize = (fso.GetFolder(src_path).Size / MB)
        destspace = psutil.disk_usage("F:\\_FOTOGRAFIE").free / MB

        print("---------------------------")
        print(" Foldername:   %s" %folder)
        print(" Year:         %s" %folderyear)
        print(" Size:         %.2f MB" %srcfoldersize)
        print(" Copying from %s to %s" %(src_path, dest_path))

        if srcfoldersize > destspace:
            print(" Not enough Space in Destination")
        elif os.path.exists(dest_path):
            print(" Path already existing. Skipping ...")
        else:
            shutil.copytree(src_path, dest_path)
            print(" Copy complete, opening Explorer")
            subprocess.Popen(r'explorer /select, "' + dest_path + '\\"')

        print("---------------------------")
        print(" ")



def listfiles(folder, filetype):
    pass

def renamefolder():
    pass

