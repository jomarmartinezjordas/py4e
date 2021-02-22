fname = 'mbox.txt'
fh = open(fname)

for line in fh :
    if not line.startswith('From'): continue
    pieces = line.split()
    organization = pieces[1].split('@')
    org = organization[1]
    print(org)