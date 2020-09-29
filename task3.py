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

"""
l=1
while l== 1:
    n = float(input( "give me  a number "))
    if n % 2==0:
        print("That is an even integer")
        l=0
    else:
        print("That is not an even integer")