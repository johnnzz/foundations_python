# -------------------------------------------------#
# Title: CustomerApp
# Dev:   RRoot
# Date:  12/12/2020
# Desc: This application manages customer data
# ChangeLog:
#   John Navitsky, 8/19/2016,
#   * Refactored to process customers
#   * add read and print existing data
#   * use greatest id found in file, if present
#   * add empty file error handling
#   * ensure header only written once to file
#   * don't ask to save if no data entered
#   * add gross level error handling around data entry
#
# -------------------------------------------------#
if __name__ == "__main__":
    import DataProcessor, Customers
else:
    raise Exception("This file was not created to be imported")

# -- Data --#
# declare variables and constants
objE = None  # an Customer object
intId = 0  # an CustomerId
gIntLastId = 0  # Records the last CustomerId used in the client
strFirstName = ""  # an Customers's first name
strLastName = ""  # an Customers's last name
strInput = ""  # temporary user input
isFileData = False # track if there is already data in the file

# -- Processing --#
# perform tasks
def ProcessNewCustomerData(Id, FirstName, LastName):
    try:
        # Create Customer object
        objE = Customers.Customer()
        objE.Id = Id
        objE.FirstName = FirstName
        objE.LastName = LastName
        Customers.CustomerList.AddCustomer(objE)
    except Exception as e:
        print(e)

def SaveDataToFile(isFileData):
    try:
        objF = DataProcessor.File()
        objF.FileName = "CustomerData.txt"
        if isFileData:
            # if there is already data in the file, don't write the header again
            objF.TextData = Customers.CustomerList.ToString().replace("Id,FirstName,LastName\n", "")
        else:
            objF.TextData = Customers.CustomerList.ToString()
        objF.SaveData()
    except Exception as e:
        print(e)

def EnsureExists():
    """
    append to file to ensure it exists
    """
    try:
        objF = DataProcessor.File()
        objF.FileName = "CustomerData.txt"
        objF.EnsureExists()
    except Exception as e:
        print(e)

def ReadDataFromFile():
    """
    read data from file, strip off filename
    """
    try:
        objF = DataProcessor.File()
        objF.FileName = "CustomerData.txt"
        objF.GetData()
        return(str(objF).replace(objF.FileName + ",", ""))
    except Exception as e:
        print(e)
        return("")

def FindLastId(ExistingCustomerList):
    """
    scan ids in existing string of customers to find largest id
    """
    LastId = "0"
    for CustomerLine in ExistingCustomerList.splitlines():
        CustomerData = CustomerLine.split(",")
        CustomerId = CustomerData[0]
        if str(CustomerId) > LastId and str(CustomerId) != "Id":
            LastId = CustomerData[0]
    return int(LastId)


# -- Presentation (I/O) --#
# __main__

# make sure the file exists
EnsureExists()

# read in any existing data
# show the user any existing entries
ExistingData = ReadDataFromFile()
if ExistingData:
    isFileData = True
    # print existing entries for user convenience
    print("The following customers have already been added:")
    print(ExistingData)

# update the id counter to the greatest id found in the file
gIntLastId = FindLastId(ExistingData)

# get user input
strUserInput = ""
while (True):
    strUserInput = input("Would you like to add Customer data? (y/n)")
    if (strUserInput == "y"):
        try:
            # Get Customer Id from the User
            intId = int(input("Enter an Customer Id (Last id was " + str(gIntLastId) + "): "))
            gIntLastId = intId
            # Get Customer FirstName from the User
            strFirstName = str(input("Enter an Customer First Name: "))
            # Get Customer LastName from the User
            strLastName = str(input("Enter an Customer Last Name: "))
            # Process input
            ProcessNewCustomerData(intId, strFirstName, strLastName)
        except:
            continue
    else:
        break

        # send program output


if gIntLastId > 0:
    print("The New Data is: ")
    print("----------------")
    print(Customers.CustomerList.ToString())

    # get user input
    strInput = input("Would you like to save this data to the dat file?(y/n)")
    if (strInput == "y"):
        SaveDataToFile(isFileData)
        # send program output
        print("data saved in file")
    else:
        print("data was not saved")
else:
    print("No data to save.")

print("This application has ended. Thank you!")
