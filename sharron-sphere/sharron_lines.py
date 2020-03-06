"""
===============================================================================
  Program:             sharron_lines.py
  Software Engineer:   Jonas Sharron
  Date:                27-February-2020

  Purpose: This script will ask the user for the name of a file, display the
  number of lines in the file, and then prompt the user for a line number. The
  script will then display the line entered by the user.  This script will
  repeat, asking the user which line they would like to view, until the user 
  specifies they wish to view line "0", at which point, the script will exit.
===============================================================================
"""

def file():
    """
    ===========================================================================
    Function:       file()
    Purpose:        prompt user for filename, open file, read file contents into
                    a list 
    Parameter(s):   none
    Return:         nothing; data is written to fileList[]
    ===========================================================================
    """
    
    #  set found variable to allow program to continue if invalid data file
    #  given
    found = 0
    
    #  ask for file to use, if file exists, read contents (line by line) into
    #  fileList[]; if file not found, display error and ask for input again
    while found == 0:

        file = input("Enter a the filename you wish to work with: ")
   
        try:
            f = open(file, 'r')

            for line in f:
                fileList.append(line)
                found = 1

        except FileNotFoundError:
            print("File not accessible")
    
    f.close()

#  end method file()
   
#  ============================================================================
#  create list to hold data
fileList = []
#  call method to collect file information and read data into fileList[]
file()
#  loop control variable
goAgain = 0

#  program loop to ask for and display user specified line from file (or error
#  if user input invalid); entering "0" will exit the program
while goAgain == 0:
    print("There are " + str(len(fileList)) + " lines in this file")
    
    display = input("What line would you like to view (or enter 0 to exit)? ")
    
    if int(display) < 0 or int(display) > (len(fileList)):
        print("You have picked an invalid line\n")
    elif int(display) == 0:
        goAgain = 1
    else:
        print("\n" + fileList[(int(display) - 1)])
    
#  ============================================================================
