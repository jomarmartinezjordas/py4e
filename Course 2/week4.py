'''
Week 4 : Lists

algorithms
- a set of rules or steps used to solve a problem
data structures
- a particular way of organizing data in a computer

list
- is a collection
- many values in a single variable
- surrounded by brackets, separated by commas
- can be any python object, or even another list
- can be empty

'mutable' - changeable

research about list methods

s = list() - makes an empty list
s.append() - add elements

when you add elements, it is added in order; it's also the way you can get them out.

str.sort() - means sort yourself

str.split() - breaks a string into parts and produces a list of strings


'''
friends = ['Jo', 'M', 'Ar']

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy new year,', friend)

total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + values
    count = count + 1

average = total / count
print('Average: ', average)

numblist = list()
while True :
    inp = input('Enter a number :')
    if inp =='done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)

abc = 'wtih three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

line = ' a lot        of space'
etc = line.split()
print(etc)

line2 = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

## you can also use a delimiter to guide in splitting. in this example, ';'

thing = line.split(';')
print(thing)
print(len(thing))

# spliting to get the date on the example

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
