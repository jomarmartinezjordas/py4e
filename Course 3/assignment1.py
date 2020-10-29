'''
Assignment 1: In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
'''

import re

fle = input('Enter file name here:')
if fle == '1' :
    fle = 'regex_sum_42.txt'
opn = open(fle)

tot = 0

for line in opn :
    line = line.strip()
    nbr = re.findall('[0-9]+', line)
    for val in nbr :
        val = int(val)
        tot = tot + val
print(tot)
