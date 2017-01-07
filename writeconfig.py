import configparser

def writeconfig():
    config = configparser.RawConfigParser()
    config.add_section('Foldersettings')
    config.set('Foldersettings', 'camerapath', 'I:\\DCIM')
    config.set('Foldersettings', 'archivepath', 'F:\\_FOTOGRAFIE\\__K-1_Archiv')

    config.add_section('Renditionsettings')
    config.set('Renditionsettings', 'longpixels', '2000')
    config.set('Renditionsettings', 'archivepath', 'F:\\_FOTOGRAFIE\\__K-1_Archiv')

    with open('config.cfg', 'wb') as configfile:
        config.write(configfile)


writeconfig()

