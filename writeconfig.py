import configparser

def writeconfig():
    config = configparser.RawConfigParser()
    config.add_section('Folder')
    config.set('Foldersettings', 'camerapath', 'I:\\DCIM')
    config.set('Foldersettings', 'archivepath', 'F:\\_FOTOGRAFIE\\__K-1_Archiv')

    config.add_section('Renditions')
    config.set('Renditionsettings', 'longpixels', '2000')

    with open('config.cfg', 'wb') as configfile:
        config.write(configfile)


writeconfig()

