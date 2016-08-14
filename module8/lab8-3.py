class person():

    # fields

    #firstname = None
    #lastname = None

    # constructor

    def __init__(self, firstname = "", lastname = ""):
        self.__firstname = firstname
        self.__lastname = lastname

    # properties

    # getter or accessor
    @property
    def firstname(self):
        return self.__firstname.strip().capitalize()

    # settor or mutator
    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    # getter or accessor
    @property
    def lastname(self):
        return self.__lastname.strip().capitalize()

    # settor or mutator
    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    # methods

    def to_string(self):
        return self.firstname + " " + self.lastname


myguy = person("fred", "jones")

print(myguy.to_string())

otherguy = person(lastname = "smith", firstname = "sue")

print(otherguy.to_string())