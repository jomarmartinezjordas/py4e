'''
Exer 8.5 Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line
'''

fle = input('Enter file name: ')
opn = open(fle)
cntlin = 0

for line in opn :
    line = line.strip()
    if not line.startswith('From:') : continue
    spllne = line.split(' ')
    print(spllne[1])
    cntlin = cntlin + 1

print('There were ', cntlin,' lines in the file with From as the first word.')
