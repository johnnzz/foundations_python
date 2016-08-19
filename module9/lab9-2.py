import Employees

if __name__ != "__main__":
    raise Exception("test.py is not a module and is intended to be called directly.")

Employee = Employees.Employee()
Employee.Id = 1
Employee.FirstName = "Joe"

print(Employee)