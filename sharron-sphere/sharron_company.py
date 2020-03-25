"""
Extends Person class to introduce Customer and Employee classes which are
representations of Customer and Employee.
"""

from person import Person

class Customer(Person):

    def __init__(self, name, address, phone, credit_score):
        """
        Constructor; stores customer name, address, phone, and credit score.
        """
        Person.__init__(self, name, address, phone)
        self._credit_score = credit_score

    def set_credit_score(self, credit_score):
        """
        Sets the customer's credit score.
        """
        self._credit_score = credit_score

    def get_credit_score(self):
        """
        Returns the customer's credit score.
        """
        return self._credit_score

    def __str__(self):
        """
        Returns string representation of Customer.
        """
        return "name: " + str(self.get_name()) + "\n" + \
            "address: " + str(self.get_address()) + "\n" + \
            "phone: " + str(self.get_phone()) + "\n" + \
            "credit_score: " + str(self._credit_score)

class Employee(Person):
    def __init__(self, name, address, phone, badge, salary):
        """
        Constructor; stores employee name, address, phone, badge, and salary.
        """
        Person.__init__(self, name, address, phone)
        self._badge = badge
        self._salary = salary

    def set_badge(self, badge):
        """
        Sets employee badge.
        """
        self._badge = badge

    def get_badge(self):
        """
        Returns employee badge
        """
        return self._badge

    def set_salary(self, salary):
        """
        Sets employee salary.
        """
        self._salary = salary

    def get_salary(self):
        """
        Returns employee salary.
        """
        return self._salary

    def __eq__(self, other):
        """
        Overrides "==" operator to match Employee badge attribute.
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self._badge == other._badge

    def __str__(self):
        """
        Returns string representation of Employee.
        """
        return "name: " + str(self.get_name()) + "\n" + \
        "address: " + str(self.get_address()) + "\n" + \
        "phone: " + str(self.get_phone()) + "\n" + \
        "badge: " + str(self._badge)