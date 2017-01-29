import util, copy_sd2hd


def welcomescreen():
    print "| Select an Option"
    print "|  (c) Copy SD-Card to Hard Disk"
    print "|  (f) Create Folderstructure"
    print "|  (s) Settings"
    print "|  (x) Exit"


def getselection():
    selection = raw_input('|> ')
    return selection


def copy_sd():
    util.copy_sd2hd()


def settings():
    print "entering settings"


def create_folderstructure():
    emptyfolders = util.listemptyfolders(util.archive_path)
    for item in emptyfolders:
        util.createfolders(item)


def runoption(option):
    if option == 'c':
        copy_sd()
    elif option == 'f':
        create_folderstructure()
    elif option == 's':
        settings()
    elif option == 'x':
        exit()

while True:
    welcomescreen()
    runoption(getselection())


'''
copy_sd2hd()

create_directory_structure(eventname)

copy_directory2folders()

create_lowrespictures()

create_zip()
'''



