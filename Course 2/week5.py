'''
list vs dictionaries
- linear collection of values that stay in ORDER vs a 'bag' of values, each with its own label

dictionaries are mutable

you can make dictionaries using curly brackets
jjj = { 'chuck' : 1, 'fred' : 2, 'jan' : 3}

chuck, fred and jan are called keys
1,2,3 are the values
jjj is the dictionary variable

you can also make use of for loops to count for key number and keys in the dictionary

on using two iteration variables


'''

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])

#counting with dictionaries

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
ccc['cwen'] = ccc['cwen'] + 1
print(ccc) # this will print this >> {'csev' : 1, 'cwen' : 2}

#setting an empty dictionary to have keys in it

counts = dict()
names = ['csev', 'cwen', 'csev']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# the get method for dictionaries

if name in counts :
    x = counts[name]
else :
    x = 0

x = counts.get(name, 0)

#simplified version
counts = dict()
names = ['csev', 'cwen', 'csev']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# reading a super long 3 paragraph article

counts = dict() # 1) make a dictionary
print('enter a line of text:')
line = input('') # where the people would input the text. Note(challenge): make a code that will take in a text

words = line.split() #split the line so that words would be indexed

print('Words: ', words)

print('Counting...')
for word in words :
    count[word] = counts.get(word, 0) + 1 #set up the code that would read the set of words in the article
print('Counts', counts)

#using for loops to get into dictionaries

counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts :
    print(key, counts[key]) #>> this prints jan 100 chuck 1 fred 42

#retrieving list of keys and values using dict.keys(), dict.values(), and dict.items

jjj = { 'chuck' : 1, 'fred' : 2, 'jan' : 3}
print(jjj.keys()) #>>> this should result into: ['jan', 'chuck', 'fred']
print(jjj.values()) #>>> this should result into: [1, 2, 3]
print(jjj.items()) #>> this should result into [('jan', 1), ('chuck', 2), ('fred', 3)]

#using two iteration variables

jjj = { 'chuck' : 1, 'fred' : 2, 'jan' : 3}
for aaa, bbb in jjj.items() : # aaa is the iteration variable for the keys and bbb is the iteration variable for your values
    print(aaa, bbb)

# the first example in the specialization

name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word , 0) + 1

bigcount = None
bigwords = None
for word, count in counts.items() :
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword, bigcount)
