import logging
import math
import time
import requests
import mimetypes
from multiprocessing import Pool
import os
import json
import argparse
from filechunkio import FileChunkIO

url = "http://192.168.1.13:5000/"
uploadstat = {}
logger = logging.getLogger("File-Upload-Chunks")
parser = argparse.ArgumentParser(description="Transfer large files to in chinks to FTP",
        prog="File-Upload-Using-Chinks")
parser.add_argument("src", type=file, help="The file to transfer")
parser.add_argument("dest", help="The S3 destination object")
parser.add_argument("-np", "--num-processes", help="Number of processors to use",
        type=int, default=2)
parser.add_argument("-s", "--split", help="Split size, in Mb", type=int, default=50)
parser.add_argument("-t", "--max-tries", help="Max allowed retries for http timeout", type=int, default=5)
parser.add_argument("-v", "--verbose", help="Be more verbose", default=False, action="store_true")
parser.add_argument("-q", "--quiet", help="Be less verbose (for use in cron jobs)", default=False, action="store_true")

def upload_part_from_file(fp, part_num):
    fname = 'part'+ str(part_num)
    files = {'filename': (fname, fp, 'application/octet-stream')}
    urls = url + 'fileupld/'
    print 'The URL is', urls
    r = requests.post(urls, files=files)
    m = json.loads(r.content)
    if m.get('status', ' ') == 'complete':
        return 1
    else:
        return 0
        

def upload_part(part_num, fname, offset, bytes1, amount_of_retries=10):
    """
    Uploads a part with retries.
    """
    #print 'Now uploading', fname

    def _upload(src, offset, bytes1, part_num, retries_left=amount_of_retries):
        print 'Started upload', src, offset, bytes1
        try:
            logging.info('Start uploading part #%s ...' % src)
            with FileChunkIO(src, 'r', offset=offset, bytes=bytes1) as fp:
                uploadstat[str(part_num)] = 0
                uploadstat[str(part_num)] = upload_part_from_file(fp, part_num)
            #break
        except Exception as exc:
            print 'Exception', exc
            if retries_left:
                _upload(retries_left=retries_left - 1)
            else:
                logging.info('... Failed uploading part #%d' % exc)
                print exc
                return 0
                 
        else:
            logging.info('... Uploaded part #%d' % part_num)
             
            

    _upload(fname, offset, bytes1,part_num, amount_of_retries )
    return part_num
 

def callback(x):
    logging.info('Successfully Uploaded part #%d' % x)
    if x > 0:
        uploadstat[str(x)] = 1


def measure_time(starttime, source_size):
    t2 = time.time() - starttime
    s = source_size/1024./1024.
    logger.info("Finished uploading %0.2fM in %0.2fs (%0.2fMBps)" % (s, t2, s/t2))
    
        
def main(src, dest, num_processes=2, split=50, verbose=False, quiet=False, max_tries=5):

    source_size = os.stat(src.name).st_size
    t1 = time.time()
    filenames = os.path.basename(src.name)
    if source_size  < 5*1024*1024:
        src.seek(0)
        files = {'filename': (filenames , src, 'application/octet-stream')}
        r = requests.post(url, files=files)
        m = json.loads(r.content)
        if m.get('status', ' ') == 'complete':
            measure_time(t1, source_size)
        return 0

    bytes_per_chunk = max(int(math.sqrt(5242880) * math.sqrt(source_size)),
        5242880)
    chunk_amount = int(math.ceil(source_size / float(bytes_per_chunk)))
    #import ipdb;ipdb.set_trace()
    part_num = 0
    pool = Pool(processes=num_processes)
    for i in range(chunk_amount):
        offset = i * bytes_per_chunk
        remaining_bytes = source_size - offset
        bytes1 = min([bytes_per_chunk, remaining_bytes])
        part_num = i + 1
        pool.apply_async(upload_part, (part_num, src.name, offset, bytes1, ), callback=callback)
        

    pool.close()
    pool.join()
    for worker in pool._pool:
        assert not worker.is_alive()
    if len(uploadstat) > 1:
        if 0 not in uploadstat :
            #print 'File upload complete, Now starting file combine'
            urlc = url + 'fileupld/' + 'combine/'
            r = requests.post(urlc, data = {'filename': filenames, 'filesize': source_size })
            m = json.loads(r.content)
            if m.get('status', ' ') == 'Success':
                measure_time(t1, source_size)
                return 0
        else:
            print 'File upload is incomplete'
            return 1

if __name__ == "__main__":
    fh = logging.FileHandler('oraclefile.log')
    logging.basicConfig(level=logging.INFO)
    args = parser.parse_args()
    arg_dict = vars(args)
    if arg_dict['quiet'] == True:
        logger.setLevel(logging.WARNING)
    if arg_dict['verbose'] == True:
        logger.setLevel(logging.DEBUG)
    logger.debug("CLI args: %s" % args)
    main(**arg_dict)
