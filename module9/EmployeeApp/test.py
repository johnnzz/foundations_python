import Employees, DataProcessor

if __name__ != "__main__":
    raise Exception("test.py is not a module and is intended to be called directly.")

print("test of Employees.Employee().  you should see the output 'Smith,Joe':")
Employee = Employees.Employee()
Employee.Id = 1
Employee.FirstName = "Joe"
Employee.LastName = "Smith"
print(Employee)

print()

print("test of DataProcessor.File().  you should see the output 'save this text'")
MyFile = DataProcessor.File("data.txt", "save this text")
DataProcessor.File.SaveData(MyFile)
print(DataProcessor.File.GetData(MyFile))
