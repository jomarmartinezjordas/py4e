import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = 'mbox.txt'
fh = open(fname)

for line in fh :
    if not line.startswith('Author'): continue
    pieces = line.split()
    organization = pieces[1].split('@')[1]
    org = organization.split('.')[0]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None :
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')
conn.commit()

cur.close()