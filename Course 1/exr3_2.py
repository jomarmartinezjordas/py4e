# Exer 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

score = input("Enter Score: ")
scr = float(score)
if (scr > 1.0):
    print('Score is out of range.')
elif (scr >= 0.9 and scr == 1) :
	print('A')
elif (scr >= 0.8 and scr < 0.9) :
	print('B')
elif (scr >= 0.7 and scr < 0.8) :
    print('C')
elif (scr >= 0.6 and scr < 0.7) :
    print('D')
elif (scr < 0.6) :
 print('F')
