"""
===============================================================================
  Program:             sharron_lookup.py
  Software Engineer:   Jonas Sharron
  Date:                04-March-2020

  Purpose: This script will ask yhe user if they want to view a phone number or
  address associated with an individual.  Once the user has speciefied what 
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
        
    #  open datafile; read each line into dictionary seperating out name as the
    #  key (the entire line represents the value);  inclued try/catch block
    #  incase file is inaccessable 
   
    try:
        f = open(datafile, 'r')

        for line in f:
            line = line.strip('\n')
            keyList = line.split(',', 1)
            people[keyList[0]] = line            

    except FileNotFoundError:
        print("datafile not accessible")
    
    return people
    f.close()

    #  end file() method
    #  ========================================================================

def output(search):
    """
    ===========================================================================
    Function:       output()
    Purpose:        
    Parameter(s):   
    Return:         
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

    file()
    option = 0
    global nameInfo
    nameInfo = []

    while option == 0:
        search = input("Lookup (1) phone numers or (2) addresses: ")
        if search.isalpha():
            print("Invalid selection, please choose 1 or 2")
        elif (int(search) < 1) or (int(search) > 2):
            print("Invalid selection, please choose 1 or 2")
        else:
            option = 1

        option2 = 0
        while option2 == 0:
            name = input("Enter space-seperated first and last name: ")
            if name == "":
                option2 = 1
            else:
                nameInfo = people[name].split(",")
                output(search)
                # call output

                #if int(search) == 1:
                #    print("Phone:\t" + nameInfo[5])
                #else:
                #    print("Street:\t\t" + nameInfo[1])
                #    print("City:\t\t" + nameInfo[2])
                #    print("State:\t\t" + nameInfo[3])
                #    print("Zip Code:\t" + nameInfo[4])
                #


     
   


    #  end main() method
    #  ========================================================================

if __name__== "__main__":
    main()
    

