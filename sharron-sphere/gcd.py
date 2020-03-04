"""
===============================================================================
  Program:             gcd.py
  Software Engineer:   Jonas Sharron
  Date:                05-February-2020

  Purpose: This script will calculate the gcd of two (user supplied) integers.
===============================================================================
"""

#  print banner and instructions
print("This program will calculate the gcd of two integers, please enter two") 
print("integers, the smaller one first and the gcd will be calculated")
print("======================================================================")

#  gather user input
small = input("Please enter the smaller of the two numbers: ")
large = input("Please enter the larger of the two numbers: ")
smallgcd = int(small)
largegcd = int(large)

#  test to ensure user input is positive
if smallgcd > 0 and largegcd > 0:
    #  test to ensure user data is entered in the correct order
    if smallgcd > largegcd:
        print("ERROR: the first number entered is larger than the second")
    #  Euclid's algorithm to calculate gcd
    else:
        while smallgcd > 0:
            # step 1
            div = (largegcd%smallgcd)
            # step 2
            largegcd = smallgcd
            smallgcd = div

        print("The gcd of " + small + " and " + large + " is " + str(largegcd))
else:
    print("ERROR: the numbers entered must be positive")
#  ============================================================================