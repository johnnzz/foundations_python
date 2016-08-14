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

    # override __str__ to call to_string method
    def __str__(self):
        return self.to_string()

class customer(person):

    # constructor

    # need to allow the input of a new parameter, id
    def __init__(self, id = "", firstname = "", lastname = ""):
        super().__init__(firstname,lastname)
        self.id = id

    # properties

    # getter or accessor
    @property
    def id(self):
        return self.__id

    # settor or mutator
    @id.setter
    def id(self, value):
        self.__id = value

    # methods

    def to_string(self):
        return str(self.id) + "," + self.lastname + "," + self.firstname

    def __str__(self):
        return self.to_string()


myguy = customer(20, "fred", "jones")
#myguy.id = 30


print(myguy)

