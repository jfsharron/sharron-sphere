"""
===============================================================================
  Program:             sharron_phones.py
  Software Engineer:   Jonas Sharron
  Date:                10-February-2020

  Purpose: This script will look up the corresponding phone number for wither a 
  (user supplied) last name or first and last name.  The script will retrieve
  the phone number from an external data file - phones.txt.
===============================================================================
"""

#  collect name to look up from user
name = input("Enter a last name, or first and last name (separated by a space): ")
#  convert user input to lowercase and split string into list
lowName = name.lower()
lowNameList = lowName.split()
#  determine if user has input first or first and last name and create name
#  variables (or print error message if input is incorrect)
if len(lowNameList) == 1:
    nameLength = 1
    last_name = lowNameList[0]
elif len(lowNameList) == 2:
    nameLength = 2
    first_name = lowNameList[0]
    last_name = lowNameList[1]
elif len(lowNameList) <= 0 or len(lowNameList) > 2:
    nameLength =3
    print("You have make an error in your input")

#  open data file
f = open("phones.txt", 'r')
#  message to print if input incorrect
if nameLength == 3:
    print("Program Exiting")
#  read data from file, line by line, convert data to lowercase (just as user 
#  input) to facilitate matching regardless of case and create list (both lower
#  case and as read from file (for print output))
else:
    while True:
        line = f.readline()
        if line == "":
            break
        lineList = line.split()
        searchLine = line.lower()
        searchLineList = searchLine.split()
    #  search for match to user input (if statement when user input last name; else
    #  statement if user input first and last name)
        if nameLength == 1:
            if searchLineList[1] == last_name:
                print(lineList[0] + " " + lineList[1] + ", " + 
                      searchLineList[2])
        else:
            if (searchLineList[0] + searchLineList[1]) == (first_name + last_name):
                print(lineList[0] + " " + lineList[1] + ", " + 
                      searchLineList[2])