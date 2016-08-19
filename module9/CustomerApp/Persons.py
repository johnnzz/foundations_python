# ------------Persons.py Module ---------------#
# Desc:  Classes that hold Personal data
# Dev:   RRoot
# Date:  12/12/2020
# ChangeLog:
#   8/19/2016, John Navitsky, Added LastName
# ---------------------------------------------#
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


# --- Make the class ---
class Person(object):
    """ Base Class for Personal data """
    # -------------------------------------#
    # Desc:  Holds Personal data
    # Dev:   RRoot
    # Date:  12/12/2020
    # ChangeLog:(When,Who,What)
    # -------------------------------------#

    # --Fields--
    __Counter = 0  # Hey Devs, please consider this a private class field. Thx!

    # --Constructor--
    def __init__(self, FirstName="", LastName=""):
        # Attributes
        self.__FirstName = FirstName  # Private Attribute
        self.__FirstName = LastName  # Private Attribute
        Person.__SetObjectCount()  # Private Method

    # --Properties--

    # FirstName
    @property  # getter(accessor)
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter  # (mutator)
    def FirstName(self, Value):
        self.__FirstName = Value

    # LastName
    @property  # getter(accessor)
    def LastName(self):
        return self.__LastName

    @LastName.setter  # (mutator)
    def LastName(self, Value):
        self.__LastName = Value

    # --Methods--
    def ToString(self):
        """Explictly returns field data"""
        return self.LastName + "," + self.FirstName

    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()

    @staticmethod
    def GetObjectCount():  # You do not need the self keyword
        return Person.__Counter

    @staticmethod
    def __SetObjectCount():  # This is a private and static method
        Person.__Counter += 1

        # --End of class Person--
