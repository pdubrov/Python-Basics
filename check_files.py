import os

print(os.getcwd())
#os.chdir('/Users/pilgrim/diveintopython3/examples')

print(os.path.expanduser('~'))

print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))

pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
print(os.path.split(pathname))
(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)
(shortname, extension) = os.path.splitext(filename)
print(shortname)
print(extension)

######################################
# glob accepts unix-like wildcards

import glob
print(glob.glob("*"))

metadata = os.stat('check_dicts.py')
print(metadata)
print(metadata.st_mtime)

import time
print(time.localtime(metadata.st_mtime))

#Absolute path
print(os.path.realpath('check_dicts.py'))

# read lines from file
lines = list(open('C:\Dev\Py\examples/barca.txt', encoding='utf-8'))
print(lines)

lines = [line.rstrip() for line in lines ]
print(lines)

