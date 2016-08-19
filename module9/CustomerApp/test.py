import Customers, DataProcessor

if __name__ != "__main__":
    raise Exception("test.py is not a module and is intended to be called directly.")

print("test of Customers.Customer().  you should see the output 'Smith,Joe':")
Customer = Customers.Customer()
Customer.Id = 1
Customer.FirstName = "Joe"
Customer.LastName = "Smith"
print(Customer)

print()

print("test of DataProcessor.File().  you should see the output 'save this text'")
MyFile = DataProcessor.File("data.txt", "save this text")
DataProcessor.File.SaveData(MyFile)
print(DataProcessor.File.GetData(MyFile))
