#Source: https://stackoverflow.com/questions/74892413/why-this-typeerror-msg-in-python3-script-checking-files-timestamps
from datetime import datetime as dt
import os , send2trash, timedelta

myuser=os.getlogin()

# set paths
archivePath=rf"C:\Users\{myuser}\Pictures\Saved Pictures\2022.11.zip"
logPath=rf"C:\Users\{myuser}\Downloads\screenshots\TEST"

# a list of ONLY old files based on 'last modified' time (since Epoch).
if os.path.isfile(archivePath):
    print("Archive already exists, deleting copies in TEST folder.\n")
    os.chdir(logPath)
    old=[]
    for file in sorted(os.listdir(logPath)):
        modified=dt.fromtimestamp(os.stat(file).st_mtime) ## a float nr?
        ## conditions to be met: 
        if modified.date() <= dt.date(2022,4,30):
           old.append(file)
        else:
            print(str(file), ': conditions NOT met.')
    ## mv to trashcan
    numberFiles=len(old)
    print(f"Deleting {numberFiles} file.")
    for oldFile in old:
        send2trash.send2trash(oldFile)
else:
    print('No files deleted.')