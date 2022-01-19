#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
You may need to use the:
print( variable , end='') option to print on one line
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
x = input('enter a number')
numlist = [1,2,3,4,5,6,7,8,9,10,11,12]
x = int(x)
for i in numlist:
    print(i * x, end = " ")



