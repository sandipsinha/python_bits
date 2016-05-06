# Import required python libraries
import os
import time
import datetime
import sys
from tempfile import mkstemp
from shutil import move
from os import remove, close
import re


BACKUP_PATH = '/Users/ssinha/pythonplay/'


# Getting current datetime to create seprate backup folder like "12012016-071334".
DATETIME = time.strftime('%Y%m%d-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH

##def make_upload_file_ready(tname, delim):
##    fh, abs_path = mkstemp()
##    flname = tname + '.sql'
##    expres = '\\' + delim  
##    with open(abs_path,'w') as new_file:
##        with open(os.path.join(TODAYBACKUPPATH, flname),'r') as old_file:
##            for line in old_file:
##                line2 = line.replace("\\", "\\\\").replace(delim,expres)
##                replaced = '\\' + line2 if line2.find("\\") != 0 else line2
##                new_file.write(replaced)
##    close(fh)
##    #Remove original file
##    remove(os.path.join(TODAYBACKUPPATH, flname))
##    #Move new file
##    move(abs_path, os.path.join(TODAYBACKUPPATH, flname))
##
##    return True

def update_and_check(tname, delim):
    fh, abs_path = mkstemp()
    flname = tname + '.sql'
    expres = '\\' + delim  
    with open(abs_path,'w') as new_file:
        with open(os.path.join(TODAYBACKUPPATH, flname),'r') as old_file:
            for line in old_file:
                line2 = line.replace("\\\\", "\\").replace(expres,delim)
                replaced = line2.replace("\\","",1) if line2.find("\\") == 0 else line2
                new_file.write(replaced)
    close(fh)
    #Remove original file
    remove(os.path.join(TODAYBACKUPPATH, flname))
    #Move new file
    move(abs_path, os.path.join(TODAYBACKUPPATH, flname))

    return True

def create_file(tname):
    try:
        # Checking if backup folder already exists or not. If not exists will create it.
        print "creating backup folder"
        if not os.path.exists(TODAYBACKUPPATH):
            os.makedirs(TODAYBACKUPPATH)
        flname = tname + '.sql'

        print "opening file for processing."
        file1 = open(os.path.join(TODAYBACKUPPATH, flname),'r')

        print "Starting backup of the given TB" + tname

    except (OSError, IOError) as e:
        print "File create error({0}): {1}".format(e.errno, e.strerror)
        return None

    else:
        return file1

if __name__ == "__main__":
    tname = 'testFile'
    delim = ','
    getafile = create_file(tname)
    getafile.close()
    update_and_check(tname, delim)
