class person():

    firstname = None
    lastname = None

    def to_string(self):
        return self.firstname + " " + self.lastname

myguy = person()
myguy.firstname = "fred"
myguy.lastname = "jones"

print(myguy.to_string())