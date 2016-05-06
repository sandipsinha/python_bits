import os, sys
readsize = 1024
import glob

@app.route('/close/', methods=['POST'])
def complete_upload(tofile):
    output = open(tofile, 'wb')
    parts  = os.listdir(config.tempdir)
    parts.sort(  )
    for filename in parts:
        filepath = os.path.join(config.tempdir, filename)
        fileobj  = open(filepath, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close(  )
    output.close(  )

@app.route('/total_upload/filename', methods=['POST'])
def get_size():
    total_size = 0
    fileString = config.tempDir + '/' + filename + '*'
    for f in glob.glob(fileString):
        if os.path.isfile(f):
            fp = os.path.join(config.tempDir, f)
            total_size += os.path.getsize(fp)
    return jsonify ({"File_size":total_size})

@app.route('/upload/', methods=['POST'])
def upload(filename):
    


