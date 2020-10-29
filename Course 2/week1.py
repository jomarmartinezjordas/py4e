#Week 1
'''
# len() - counts the number of indices on a string

fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Using for & in

fruit = 'banana'
for letter in fruit :
    print(letter)

# slicing strings
s = 'jomar jordas'
print(s[:])

# >>note that the brackets mean 'up to but not including'

# Using in as a logical operator
print('Is the letter found in banana?')
fruit = 'banana'
n = input('Enter a letter: ')
try :
    n = str(n)
except :
    print('Please enter a letter')
if n in fruit :
    print('Yes')
else :
    print('No')

# Using string libraries
# - functions that are already built into every string >> we invoke using .funtion()

word = input('Enter a word: ')
fnd = input('Enter a letter: ')
def pos(fin) :
    fin = word.find(fnd)
    return fin

print(pos)

ans = input('Do you want to change the word? Answer Yes or No: ')
if ans == 'Yes' :
    word = input('Enter a word: ')
    fnd = input('Enter a letter: ')

print(pos)
'''
