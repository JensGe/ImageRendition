# -*- coding: utf-8 -*-

import os

def checkwhichfolder():
    archive_path = os.path.abspath("F:\\_FOTOGRAFIE\\__K-1_Archiv")
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


checkwhichfolder()
