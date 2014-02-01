from picLib import FileInfoExtractor

f = FileInfoExtractor('test.py')
f.floodMetaData()
print('FileName:' + getattr(f,'filename'))
print('Type: '+ getattr(f,'type'))
print('IsValidFile:' + str(getattr(f, 'validFile')))
print('FileSize: ' + str(getattr(f, 'size')) + " Byte")
print('DateInfo:'  + getattr(f, 'date'))