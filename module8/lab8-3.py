class person():

    # fields

    firstname = None
    lastname = None

    # constructor

    def __init__(self, firstname = "", lastname = ""):
        self.firstname = firstname
        self.lastname = lastname

    # properties

    # methods

    def to_string(self):
        return self.firstname + " " + self.lastname


myguy = person("fred", "jones")

print(myguy.to_string())

otherguy = person(lastname = "smith", firstname = "sue")

print(otherguy.to_string())