'''
Exer 7.2 Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

Expected output:
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519


'''
fle = input('Enter file name: ')
count = 0
totl = 0

try :
    opn = open(fle)

except:
    print('File not found.')
    quit()

for line in opn :
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence') :
        fgs = len(line)
        avg = line[19:fgs+1]
        avg = float(avg)
        count = count + 1
        totl = totl + avg

print('Average spam confidence:', totl/count)
