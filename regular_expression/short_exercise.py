import re

fname = input('Enter the file name: ')
try:
    fh = open(fname, 'r')
except:
    print('file cannot be opened: ', fname)
    quit()
print( sum([int(var) for var in re.findall(r'[0-9]+', fh.read()) ] ) )
