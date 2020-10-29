# Week 3
'''
Files
handle = open('filename', 'mode'); mode can be w or r [read or write]
\n - > new line

str.read() - reads the whole file (newlines and all into a single string)
str.startswith() -

--- print function adds a newline automatically at the end of a line
str.rstrip() - used to remove whitespace from print() because it is on the right

quit()

'''

fhand = open('insert file name here')
count = 0
for line in fhand :
    count = count + 1
print('Line count:', count)

###

fhand = open('insert filename here')
inp = fhand.read()
print(len(inp))

###

fhand = open('insertfilename here')
for line in fhand
    if line.startswith('') :
        print(line)

###

fhand = open('insert filename here')
for line in fhand :
    line = line.rstrip()
    if line.startswith() :
        print(line)

### bad file names

fname = input('Enter the file name: ')
try :
    fhand = open(fname)
except :
    print('File cannot be opened', fname)
    quit()

count = 0
for line in fhand :
    if line.startswith('Subject:')
        count = count + 1
print('There were', count, 'subject lines in', fname)
