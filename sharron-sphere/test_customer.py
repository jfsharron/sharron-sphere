"""
File: test_customer.py
This is a test program for the Customer class defined in module customer.py
"""

# Import the Customer class from the customer.py module
from customer import Customer

# Create an instance of a customer class.
c = Customer("Josh Kelly", "7416 Monroe Ave., Media, PA, 19063", "424-555-4053")

# Display the state of the newly created customer object.
print(c)

# Ask the user for a new phone number of the customer
new_phone = input("\nEnter a new phone number for Josh Kelly: ")
c.set_phone(new_phone)

# Display the customer's new phone number
print("\nJosh's new number is ", c.get_phone())

# Display all of the customer's information.
print("\nJosh's new information is ", c)

