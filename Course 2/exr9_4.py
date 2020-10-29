'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

fle = input('Enter file name: ')
opn = open(fle)
sender = []
email = dict()

for line in opn :
    line = line.strip()
    if not line.startswith('From ') : continue
    line = line.split()
    sender.append(line[1])

for address in sender :
    email[address] = email.get(address, 0) + 1

most_email = None
most_nbr = None

for address, nbr in email.items() :
    if most_email is None or nbr > most_nbr :
        most_email = address
        most_nbr = nbr

print(most_email, most_nbr)
