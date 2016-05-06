#!/usr/bin/python
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump utility.
#
# Written by : Sandip Sinha
#
##########################################################

# Import required python libraries
import os
import time
import datetime
import sys
from tempfile import mkstemp
from shutil import move
from os import remove, close

BACKUP_PATH = '/Users/ssinha/pythonplay/dbbackup/'


# Getting current datetime to create seprate backup folder like "12012016-071334".
DATETIME = time.strftime('%Y%m%d-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME


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
        
            
                     

def export_db_table(tname, delim):
    
    count = 0
    getOutFile = create_file(tname)
    if getOutFile:
        try:
            # Starting actual database backup process.
            if run_export_script(tname, delim):
                # Checking if the file was created with actual lines in it.
                count = len(getOutFile.readlines())
                if count > 0:
                    getOutFile.close()
                    update_and_check(tname, delim)
                    print "Backup script completed"
                    print "Your backups has been created in {0} directory".format(TODAYBACKUPPATH)
                else:
                    print "Backup script unsucessful"
            else:
                print "Backup script unsucessful"
                              
        except (OSError, IOError) as e:
            print "File create error({0}): {1}".format(e.errno, e.strerror)
        finally:
            return count
    else:
        print "File was not created"
        return 0

def run_export_script(tname, delim):
    try:
        dumpcmd = "dbexport -t " + tname + " -c "  + delim + " -r" 
        os.system(dumpcmd)
        return True
    except exception as e:
        print "Running script error({0}): {1}".format(e.errno, e.strerror)
        return False

def create_file(tname):
    try:
        # Checking if backup folder already exists or not. If not exists will create it.
        print "creating backup folder"
        if not os.path.exists(TODAYBACKUPPATH):
            os.makedirs(TODAYBACKUPPATH)
        flname = tname + '.sql'

        print "opening file for processing."
        file1 = open(os.path.join(TODAYBACKUPPATH, flname),'w')

        print "Starting backup of the given TB" + tname

    except (OSError, IOError) as e:
        print "File create error({0}): {1}".format(e.errno, e.strerror)
        return None

    else:
        return file1

if __name__ == '__main__':
    tname = raw_input('Enter the table name: ')
    dlimit = raw_input('Enter a delimiter: ')
    export_db_table(tname, dlimit)




    
    
    

        
                          
