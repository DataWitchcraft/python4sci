#############################################################################
#
# TEXT FILES
#
#############################################################################

# to know more about how to open files for reading or writing
# read https://swcarpentry.github.io/python-second-language/12-file-io/

with open('data/species.csv', 'r') as f:
    data = f.read()
print('file contains', len(data), 'bytes')
