import os.path
import datetime
import Image
import time
import sys
import shutil
from datetime import datetime

class FileInfoExtractor:
    "Determine file type and information about the filetype"
    def __init__(self, filename):
        self.filename=filename
        self.fileType()
        self.checkFile()

    def checkFile(self):
        self.validFile = os.path.isfile(self.filename)

    def fileType(self):
        self.type = ''
        if self.filename.lower().endswith('.mov'):
            self.type='MOV'
        elif self.filename.lower().endswith('.jpeg') or self.filename.lower().endswith('.jpg'):
            self.type='JPEG'
        elif self.filename.lower().endswith('mts'):
            self.type='MTS'

        return self.type

    def floodMetaData(self):
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(self.filename)
        self.ctime = ctime
        self.date = time.ctime(ctime)
        self.size = size

        if (self.type =='JPEG'):
            try:
                im = Image.open(self.filename)
                if hasattr(im, '_getexif'):
                    exifdata = im._getexif()
                    self.ctime = exifdata[0x9003]
                    print(time.ctime(self.ctime))
                    #substitute with exif time information
                    #Convert to dateobj
            except: 
                _type, value, traceback = sys.exc_info()
                #print "Error:\n%r", value
        
        #Lets create a dateobject and extract day, month and year information
        dateobj = datetime.strptime(time.ctime(self.ctime), '%a %b %d %H:%M:%S %Y')
        self.extractDateData(dateobj)


    def extractDateData(self,dateobj):
        if dateobj!=None:
            self.day = dateobj.day.__str__()
            if self.day.__len__()==1:
                self.day="%d%s" % (0,self.day)
            self.month= dateobj.month.__str__()
            if self.month.__len__()==1:
                self.month="%d%s" %(0,self.month)
            self.year = dateobj.year.__str__()

