# ------------Customers.py ---------------#
# Desc:  Classes that hold customer data
# Dev:   RRoot
# Date:  12/12/2020
# ChangeLog:(When,Who,What)
#   8/19/2016, John Navitsky, Converted to Customer
# ---------------------------------------------#
import Persons

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


# --- Make child class ---
class Customer(Persons.Person):
    """ Class for Customer data """

    # --Fields--
    # Id = Customer Id

# --Constructor--
def __init__(self, Id=""):
    # Attributes
    self.__Id = Id

# --Properties--
# Id
@property  # getter(accessor)
def Id(self):
    return self.__Id

@Id.setter  # (mutator)
def Id(self, Value):
    self.__Id = Value

# --Methods--

def ToString(self):
    """Explictly returns field data"""
    strData = super().ToString()
    return str(self.Id) + ',' + strData

def __str__(self):
    """Implictly returns field data"""
    return self.ToString()

# --End of Class Employee --

class CustomerList(object):
    """ Static class for holding a list of Customer data """

    # --Fields--
    __lstCustomers = []  # a list with Customer objects

    # --Constructor--
    # @staticmethod in python constructors cannot be static
    # def __init__():
    # Attributes

    # --Properties--
    # None

    # --Methods--
    @staticmethod
    def AddCustomer(Customer):
        if str(Customer.__class__).startswith("<class 'Customers.Customer'"):
            CustomerList.__lstCustomers.append(Customer)
        else:
            raise Exception("Only Customer objects can be added to this list")

    @staticmethod
    def ToString():  # This overrides the original method (it's polymorphic)
        """Explictly returns field data"""
        strData = "Id,FirstName,LastName\n"
        for item in CustomerList.__lstCustomers:
            strData += str(item.Id) + "," + item.FirstName + "," + item.LastName + "\n"
        return strData

@staticmethod
def __str__():  # This overrides the original method as well
    """Implictly returns field data"""
    strData = CustomerList.ToString
    return strData

# --End of Class --
