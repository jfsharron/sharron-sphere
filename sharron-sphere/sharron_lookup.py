"""
===============================================================================
  Program:             sharron_lookup.py
  Software Engineer:   Jonas Sharron
  Date:                04-March-2020
  Purpose: This script will ask the user if they want to view a phone number or
  address associated with an individual.  Once the user has specified what 
  they want to view, the user will need to supply a first and last name.  The  
  script will then look up the information from an external data file.
===============================================================================
"""

def file():
    """
    ===========================================================================
    Function:       file()
    Purpose:        open datafile, read information into dictionary
    Parameter(s):   none
    Return:         people{} dictionary
    ===========================================================================
    """

    #  define datafile and create empty dictionary
    datafile = "address.txt"
    global people
    people = {}
        
    #  open datafile; read each line into dictionary separating out name as the
    #  key (the entire line represents the value);  included try/catch block
    #  in case file is inaccessible 
   
    try:
        f = open(datafile, 'r')

        for line in f:
            line = line.strip('\n')
            keyList = line.split(',', 1)
            keyList[0] = keyList[0].lower()
            people[keyList[0]] = line       

    except FileNotFoundError:
        print("datafile not accessible")
    
    return people
    f.close()

    #  end file() method
    #  ========================================================================

def output(search = 1):
    """
    ===========================================================================
    Function:       output()
    Purpose:        format and display user requested data
    Parameter(s):   search (1 displays phone number, 2 displays address; 
                    defaults to 1)
    Return:         none; output sent to screen
    ===========================================================================
    """
    
    if int(search) == 1:
        print("Phone:\t" + nameInfo[5])
    else:
        print("Street:\t\t" + nameInfo[1])
        print("City:\t\t" + nameInfo[2])
        print("State:\t\t" + nameInfo[3])
        print("Zip Code:\t" + nameInfo[4])

    #  end method output()
    #  ========================================================================
def main():
    """
    ===========================================================================
    Function:       main()
    Purpose:        entry point for program
    Parameter(s):   none
    Return:         none
    ===========================================================================
    """

    #  call file method to open data file and read information into dictionary
    file()
    #  loop control variable to determine if lookup question (phone or address)
    #  should continue to be displayed
    option = 0
    #  list to hold information from datafile 
    global nameInfo
    nameInfo = []

    #  user entry to determine if phone or address information should be 
    #  displayed, includes try/catch block in case entry is invalid
    while option == 0:
        try:
            search = input("Lookup (1) phone numbers or (2) addresses: ")
            if search.isalpha():
                print("Invalid selection, please choose 1 or 2")
            elif (int(search) < 1) or (int(search) > 2):
                print("Invalid selection, please choose 1 or 2")
            else:
                option = 1
        except ValueError:
            print("Invalid selection, please choose 1 or 2")
            option = 0

    #  option2 loop control variable to continually ask for name to look up 
    #  (exit if user entry is blank)
    option2 = 0
    #  loop to ask for name entry
    while option2 == 0:
        name = input("Enter space-separated first and last name: ")
        lowerName = name.lower()

        if name == "":
            option2 = 1
        else:
            try:
                nameInfo = people[lowerName].split(",")
                output(search)
            except KeyError:
                print("error: person not found")

    #  end main() method
    #  ========================================================================

if __name__== "__main__":
    main()
