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


BACKUP_PATH = '/Users/ssinha/pythonplay/dbbackup/'


# Getting current datetime to create seprate backup folder like "12012016-071334".
DATETIME = time.strftime('%Y%m%d-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

def make_upload_file_ready(tname, delim):
    fh, abs_path = mkstemp()
    flname = tname + '.sql'
    expres = '\\' + delim  
    with open(abs_path,'w') as new_file:
        with open(os.path.join(TODAYBACKUPPATH, flname),'r') as old_file:
            for line in old_file:
                line2 = line.replace("\\", "\\\\").replace(delim,expres)
                replaced = '\\' + line2 if line2.find("\\") != 0 else line2
                new_file.write(replaced)
    close(fh)
    #Remove original file
    remove(os.path.join(TODAYBACKUPPATH, flname))
    #Move new file
    move(abs_path, os.path.join(TODAYBACKUPPATH, flname))

    return True


def import_db_table(tname, delim):
    
    count = 0
    getInFile = verify_file(tname)
    if getInFile:
        
        try:
            # Starting table upload process.
            make_upload_file_ready(tname, delim)
            if run_import_script(tname, delim):
                print "The file has been successfully uploaded"
                return True
            else:
                raise IOError('Upload was not successful')
                             
        except (OSError, IOError) as e:
            print "Upload error({0}): {1}".format(e.errno, e.strerror)
            return False
        else:
            return True
    else:
        print "The file was not found and could not be uploaded"
        return False

def run_import_script(tname, delim):
    try:
        dumpcmd = "dbimport -t " + tname + " -c "  + delim + " -r " 
        if os.system(dumpcmd) == 0:
            return True
        else:
            raise OSError('Upload was not successful')
    except (OSError, IOError) as e:
        print "Running import script error({0}): {1}".format(e.errno, e.strerror)
        return False

def verify_file(tname):
    try:
        # Checking if backup folder already exists or not. 
        print "Verifying input folder"
        if not os.path.exists(TODAYBACKUPPATH):
            raise IOError('No folder exists for the give file')
        flname = tname + '.sql'

        print "opening file for reading"
        file1 = open(os.path.join(TODAYBACKUPPATH, flname),'r')

        print "Successfully opened input file {0}, for reading".format(tname+'.sql')

    except (OSError, IOError) as e:
        print "File create error({0}): {1}".format(e.errno, e.strerror)
        return None

    else:
        return file1

if __name__ == '__main__':
    tname = raw_input('Enter the table name: ')
    dlimit = raw_input('Enter a delimiter: ')
    import_db_table(tname, dlimit) 
    


    
    
    

        
                          
