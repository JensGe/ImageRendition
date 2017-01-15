import os, configparser



def checkwhichfolder():
    archive_path = os.path.abspath(config.get("Foldersettings", "archivepath"))
    print archive_path
    renditionfolders = []
    for yearfolder in os.listdir(archive_path):
        for folder in os.listdir(archive_path + "\\" + yearfolder):
            if not (' ' in folder):
                fileextensions = []
                for file in os.listdir(archive_path + "\\" + yearfolder + "\\" + folder):
                    filename, fileextension = os.path.splitext(file)
                    fileextension = fileextension[1:].upper()
                    if not fileextension in fileextensions:
                        fileextensions.append(fileextension)
                print folder + ": " + str(fileextensions)
                renditionfolders.append(folder)
    print renditionfolders




config = configparser.ConfigParser()
config.read_file(open('config.cfg'))

checkwhichfolder()


def get_folders():
    folderlist = []
    return folderlist

def is_folder_without_space(folderstring):
    if (' ' in folderstring):
        return False
    if not (' ' in folderstring):
        return True

def is_dng_and_jpg_folder(folder):
    return True

def get_folder_extensions(folder):
    extensions = []
    return (extensions)