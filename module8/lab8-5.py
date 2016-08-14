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

    __last_id = 0

    # constructor

    # need to allow the input of a new parameter, id
    def __init__(self, firstname = "", lastname = ""):
        super().__init__(firstname,lastname)
        customer.__last_id = customer.__last_id + 1
        self.id = customer.__last_id

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

    @staticmethod
    def last_cust_id():
        return customer.__last_id


customer1 = customer("fred", "jones")
print(customer1)

customer2 = customer("sue", "barnes")
print(customer2)



