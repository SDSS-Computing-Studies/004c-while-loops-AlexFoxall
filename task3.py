#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer     


REPEAT while exit condition has not been met:
    enter an input
    convert input to a number
    find the remainder
    if the remainder is 0 then update exit condition

"""
number = 2

while number != 0:
    number = int(input("Enter a number: "))
    if (number % 2) != 0:
        print("That is not even integer")
            else:
                print("That is not an even integer")

        