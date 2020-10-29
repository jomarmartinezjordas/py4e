'''
Exer 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
'''

fle = input('Enter file name: ')
if fle == 1 :
    fle = mbox-short.txt
opn = open(fle)
hours = []
oras = dict()

for line in opn :
    line = line.strip()
    if not line.startswith('From ') : continue
    line = line.split()
    time = line[5]
    time = time.split(':')
    hours.append(time[0])

for hour in hours :
    oras[hour] = oras.get(hour, 0) + 1

lst = list(oras.keys())
lst.sort()
for key in lst :
    print(key, oras[key])
