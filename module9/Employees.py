# ------------Employees.py ---------------#
# Desc:  Classes that hold employee data
# Dev:   RRoot
# Date:  12/12/2020
# ChangeLog:(When,Who,What)
# ---------------------------------------------#
import Persons

if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


# --- Make child class ---
class Employee(Persons.Person):
    """ Class for Employee data """
    # -------------------------------------#
    # Desc:  Holds Employee data
    # Dev:   RRoot
    # Date:  12/12/2020
    # ChangeLog:(When,Who,What)
    # -------------------------------------#

    # --Fields--
    # Id = Employee Id

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
