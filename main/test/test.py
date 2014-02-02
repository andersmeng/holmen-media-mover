#Trick for importing at separate location in python

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..','src'))

from picLib import FileInfoExtractor

f = FileInfoExtractor('test.py')
f.floodMetaData()
print('FileName:' + getattr(f,'filename'))
print('Type: '+ getattr(f,'type'))
print('IsValidFile:' + str(getattr(f, 'validFile')))
print('FileSize: ' + str(getattr(f, 'size')) + " Byte")
print('DateInfo:'  + getattr(f, 'date'))