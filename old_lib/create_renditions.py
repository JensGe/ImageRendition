import os, configparser








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