'''
Week 2: Regular Expressions

import re:
re.search() - used to check is a string matches a regular expression
re.finalall() - used to extract portions of a string rhat match your regular expression

dot (.) character matches any character
adding the asterisk character, the character is 'any number of times'
adding forward slash - match any non-whitespace characters
addition sign (+) - one or more times
? character - not greedy, gets the shortest
\ can only used for active characters i.e. '$' to behave normally


'''
#Using re.search() like .find()
hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.find('From:') >= 0 : # this is different from below
        print(line)

###
import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('FromL', line) : ###
        print(line)

#using re.search like .startswith()

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if line.startswith('From:') : #this is differnt from below
        print(line)

###
import re

hand = open('mbox-short.txt')
for line in hand :
    line = line.rstrip()
    if re.search('^From:', line) : ###
        print(line)

#using regex symbols

^X.*: # this means 'Looking for lines with X at the beginning followed by some number of characters, followed by a colon '
^X-\S+: # this means 'Looking for lines that start with X, followed by any non-whitespace character, greater than or equal to 1 time,  followed by a colon '

#Extracting data

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)

# [0-9]+ means one or more digits

import re

line = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y =re.findall('@([^ ]*)', lin)
print(y) ## this prints ['uct.ac.za']

###

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand :
    line = line.rstrip()
    stuff = re.findall('^x-DSPAM-Confidence: ([0-9]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))
