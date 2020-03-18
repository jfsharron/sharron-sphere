"""
File:   sharron_customers.py
Resources to manage customer information.
"""

class Customer(object):
    """Represents the customer"""

    def __init__(self, name, address, phone):
        """
        Constructor to create a customer and contain their name, address, and
        phone information.
        """
        self.name = name
        self.address = address
        self.phone = phone

    def setAddress(self, address):
        """
        method for setting/resetting customer address information
        """
        self.address = address

    def setPhone(self, phone):
        """
        method for setting/resetting customer phone information
        """
        self.phone = phone

    def getName(self):
        """
        returns customer name
        """
        return self.name

    def getAddress(self):
        """
        returns customer address
        """
        return self.address

    def getPhone(self):
        """
        returns customer phone
        """
        return self.phone

    def __str__(self):
        """
        returns the string representation of the customer
        """
        return "Name: " + self.name + \
            "\nAddress: " + self.address + \
            "\nPhone: " + self.phone

