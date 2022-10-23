#############################################################################
#
# TEXT FILES
#
#############################################################################

# to know more about how to open files for reading or writing
# read https://swcarpentry.github.io/python-second-language/12-file-io/

import sys

print(sys.argv)  # list with the arguments 


# getting INPUT_FILE_NAME from the arguments, 'data/species.csv' if not given
if len(sys.argv) > 1:
    INPUT_FILE_NAME = sys.argv[1]
else:
    INPUT_FILE_NAME = 'data/species.csv'

# opening the file:
#    'r' for reading
#    'w' for writing (immediately erases existing contents)
#    'a' for appending
f = open(INPUT_FILE_NAME, 'r')
# read the whole file, write(data) writes data into file
data = f.read()
print('File', INPUT_FILE_NAME, 'contains', len(data), 'bytes.')
# do not forget to close the file (or better use with, see below)
f.close()


# `with` will guarantee that the file will be closed 
with open(INPUT_FILE_NAME, 'r') as f:
    count = 0
    for line in f:
        count = count + 1
print('File', INPUT_FILE_NAME, 'contains', count, 'lines.')


# Your turn - EXERCISE
# Try to modify the code in such a way that
# 1. It reads another parameter from the arguments - OUTPUT_FILE_NAME
# 2. It reads INPUT_FILE_NAME and then writes the content into OUTPUT_FILE_NAME
# 3. Same as 2. but add the line number in front of each line (i.e. add "1" before the first line, "2" before the second...) 
# 4. Same as 3. but skip empty lines (hint: use str.strip method), test on 'data/ls_orchid_small.fasta' file
