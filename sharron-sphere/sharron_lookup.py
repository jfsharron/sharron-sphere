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

def input():
    people = []
    f = open("address.txt", 'r')
    while True:
        line = f.readline()
        if line == "":
            break
        people = line.split()
    
    print(people)




input()