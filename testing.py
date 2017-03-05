import os


archive_path = os.path.abspath('F:\\_FOTOGRAFIE\\__K-1_Archiv')


def listdirs(folder):
    return [
        d for d in (os.path.join(folder, d1) for d1 in os.listdir(folder))
        if os.path.isdir(d)
    ]



def listemptyfolders():
    emptyfolders = []
    for yearfolder in os.listdir(archive_path):
        for folder in os.listdir(archive_path + "\\" + yearfolder):
            if listdirs(archive_path + "\\" + yearfolder + "\\" + folder) == []:
                emptyfolders.append(folder)
    return emptyfolders


print(listemptyfolders())