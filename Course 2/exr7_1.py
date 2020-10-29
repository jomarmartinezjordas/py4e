#chapter 7 exers - from book

opn = input('Enter file name to open: ')
try :
    fle = open(opn)
except :
    print('File cannot be opened / does not exist.')
    quit()

for line in fle :
    line = line.rstrip()
    print(line.upper())
    if line.endswith('-0500') : break
