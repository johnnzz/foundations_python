class person():

    # fields

    #firstname = None
    #lastname = None

    # constructor

    def __init__(self, firstname = "", lastname = ""):
        # use properties
        self.firstname = firstname
        self.lastname = lastname

    # properties

    # getter or accessor
    @property
    def firstname(self):
        return self.__firstname

    # settor or mutator
    @firstname.setter
    def firstname(self, value):
        self.__firstname = value.strip().capitalize()

    # getter or accessor
    @property
    def lastname(self):
        return self.__lastname

    # settor or mutator
    @lastname.setter
    def lastname(self, value):
        self.__lastname = value.strip().capitalize()

    # methods

    def to_string(self):
        return self.firstname + " " + self.lastname


myguy = person("fred  ", "  jones")

print(myguy.to_string())

otherguy = person(lastname = "smIth", firstname = "sue")

print(otherguy.to_string())