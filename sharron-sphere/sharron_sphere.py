"""
===============================================================================
  Program:             sharron-sphere.py
  Software Engineer:   Jonas Sharron
  Date:                28-January-2020

  Purpose: This script will calculate the diameter, circumference, surface area,
            and volume of a sphere.  The radius of the sphere will be provided
            through a user prompt.
===============================================================================
"""

import math

def diameter(radius):
    """
    ===========================================================================
    Function:        diameter(radius)
    Purpose:        calculate the diameter of a circle/sphere
    Parameter(s):   radius; the radius of the circle/sphere
    Return:         diameter
    ===========================================================================
    """
    diameter = (2 * float(radius))
    return round(diameter,2)
#  ============================================================================

def circumference(radius):
    """
    ===========================================================================
    Function:       circumference(radius)
    Purpose:        calculate the circumference of a circle/sphere
    Parameter(s):   radius; the radius of the circle/sphere
    Return:         circumference
    ===========================================================================
    """
    circumference = (2 * float(radius) * math.pi)
    return round(circumference,2)
#  ============================================================================

def surfaceArea(radius):
    """
    ===========================================================================
    Function:       surfaceArea(radius)
    Purpose:        calculate the surface area of a circle/sphere
    Parameter(s):   radius; the radius of the circle/sphere
    Return:         area
    ===========================================================================
    """
    area = (4 * math.pi * float(radius) * float(radius))
    return round(area,2)
#  ============================================================================

def volume(radius):
    """
    ===========================================================================
    Function:       volume(radius)
    Purpose:        calculate the volume of a circle/sphere
    Parameter(s):   radius; the radius of the circle/sphere
    Return:         volume
    ===========================================================================
    """
    volume = (4/3 * math.pi * float(radius) * float(radius) * float(radius))
    return round(volume,2)
#  ============================================================================

# prompt user for radius
radius = input("Please enter the radius (units) of the sphere: ")

# call functions to calculate values and print output to screen
print("\nThe diameter, circumference, surface area, and volume of the sphere \
are as follow:")
print("The diameter is " + str(diameter(radius)) + " units.")
print("The circumference is " + str(circumference(radius)) + " units.")
print("The surface area is " + str(surfaceArea(radius)) + " units.")
print("The volume is " + str(volume(radius)) + " units.")
#  ============================================================================
