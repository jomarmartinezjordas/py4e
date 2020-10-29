'''
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

pythonschoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

file = input('Enter file name: ')
open = open(file)
sender = []
domain = []
dcount = dict()

for line in open :
    line = line.strip()
    if not line.startswith('From ') : continue
    line = line.split()
    sender.append(line[1])

for dname in sender :
    dname = dname.split('@')
    domain.append(dname[1])

for count in domain :
    dcount[count] = dcount.get(count, 0) + 1

print(dcount)
