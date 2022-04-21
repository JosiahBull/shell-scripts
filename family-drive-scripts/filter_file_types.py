# ALL FILE TYPES FOUND FROM RUNNING get_file_types.py
# ['.PNG', '.JPG', '.MTS', '.URL', '.ini', '.jpg', '.db', '.mpfc', '.info', '.ppt', '.THM',
# '.avi', '.AVI', '.modd', '.moff', '.tiff', '.CRW', '.crw', '.gif', '.bmp', '.lnk', '.wmf',
# '.mid', '.wav', '.doc', '.MOV', '.MPO', '.mp4', '.ithmb', '', '.ico', '.png', '.wmv', '.CR2',
# '.mht', '.xls', '.tmp', '.pptx', '.url', '.INI', '.wma', '.MSWMM', '.exe', '.plist', '.mp3',
# '.m4a', '.itc2', '.itdb', '.itl', '.xml', '.app', '.m4v', '.wpl', '.epub', '.MP3', '.cda',
# '.docx', '.psd', '.prproj', '.cfa', '.pek', '.aep', '.txt', '.rtf', '.rg', '.pfm', '.pfb',
# '.cfg', '.lxf', '.nwp', '.wdb', '.wdq', '.inf', '.cab', '.hdr', '.bin', '.pdf', '.dll', '.EXE',
# '.gfx', '.off', '.boot', '.inx', '.dot', '.mov', '.016', '.256', '.TMP', '.pub', '.acm', '.qts',
# '.ax', '.qtx', '.DLL', '.drv', '.vwp', '.qtp', '.conf', '.ttf', '.bat', '.dat', '.manifest',
# '.cgi', '.lst', '.ssa', '.CAB', '.indexDirectory', '.indexArrays', '.indexCompactDirectory',
# '.indexGroups', '.indexHead', '.indexIds', '.indexPositions', '.indexPostings', '.indexUpdates',
# '.shadowIndexGroups', '.shadowIndexHead', '.indexPositionTable', '.indexTermIds', '.shadowIndexArrays',
# '.shadowIndexCompactDirectory', '.shadowIndexDirectory', '.shadowIndexPositionTable', '.shadowIndexTermIds',
# '.updates', '.Trashes', '.band', '.PDF', '.torrent', '.htm', '.wps', '.aem', '.map', '.sav', '.aup', '.bak',
# '.au', '.auf', '.zip', '.ipa', '.sfk', '.emf', '.rar', '.omx', '.msi', '.Exe', '.SYS', '.flv', '.LOG1',
# '.LOG2', '.blf', '.regtrans-ms', '.sig', '.pak', '.html', '.pptm', '.pst', '.DAT', '.search-ms',
# '.xlsx', '.dotx', '.xltx', '.thmx', '.glox', '.dotm', '.mpg']

import os
import sys

start_dir = "/run/media/josiah/storage/main-disk/OldFamilyDrives/"

###### FIRST WAVE ######
# move_dir = "/run/media/josiah/storage/duplicate/"
# to_remove =  ['.URL', '.ini', '.db', '.mpfc', '.info', '.ppt', '.THM',
# '.modd', '.moff','.lnk', '.wmf',
# '.doc', '.ithmb', '', '.ico', '.CR2',
# '.mht', '.xls', '.tmp', '.pptx', '.url', '.INI', '.MSWMM', '.exe', '.plist',
# '.itc2', '.itdb', '.itl', '.xml', '.app', '.wpl', '.epub', '.cda',
# '.docx', '.psd', '.prproj', '.cfa', '.pek', '.aep', '.txt', '.rtf', '.rg', '.pfm', '.pfb',
# '.cfg',  '.nwp', '.wdb', '.wdq', '.inf', '.cab', '.bin', '.pdf', '.dll', '.EXE',
# '.gfx', '.off', '.boot', '.inx', '.dot', '.016', '.256', '.TMP', '.pub', '.acm', '.qts',
# '.ax', '.qtx', '.DLL', '.drv', '.vwp', '.qtp', '.conf', '.ttf', '.bat', '.dat', '.manifest',
# '.cgi', '.lst', '.ssa', '.CAB', '.indexDirectory', '.indexArrays', '.indexCompactDirectory',
# '.indexGroups', '.indexHead', '.indexIds', '.indexPositions', '.indexPostings', '.indexUpdates',
# '.shadowIndexGroups', '.shadowIndexHead', '.indexPositionTable', '.indexTermIds', '.shadowIndexArrays',
# '.shadowIndexCompactDirectory', '.shadowIndexDirectory', '.shadowIndexPositionTable', '.shadowIndexTermIds',
# '.updates', '.Trashes', '.band', '.PDF', '.torrent', '.htm', '.wps', '.aem', '.map', '.sav', '.aup', '.bak',
# '.auf', '.ipa', '.sfk', '.emf', '.omx', '.msi', '.Exe', '.SYS', '.LOG1',
# '.LOG2', '.blf', '.regtrans-ms', '.sig', '.pak', '.html', '.pptm', '.pst', '.DAT', '.search-ms',
# '.xlsx', '.dotx', '.xltx', '.thmx', '.glox', '.dotm']

###### SECOND WAVE ######
# move_dir = "/run/media/josiah/storage/audio/"
# to_remove = ['.wav', '.mid', '.wmv', '.wma', '.mp3', '.m4a', '.MP3', '.au']

###### THIRD WAVE ######
move_dir = "/run/media/josiah/storage/to_upload/videos/"
to_remove = ['.MTS', '.avi', '.AVI', '.MOV', '.MPO', '.mp4', '.mpg']

count = 0
def walk(path):
    global count
    for file in os.scandir(path):
        if file.is_dir():
            walk(file)
        else:
            _, ext = os.path.splitext(file)
            if ext in to_remove:
                filename = os.path.basename(file)
                dest_dir = move_dir + str(count) + filename
                os.rename(file, dest_dir)
                count = count + 1


walk(start_dir)
print("moved " + str(count) + " files")