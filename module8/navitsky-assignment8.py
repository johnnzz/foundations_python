'''
1)	Create a testing a new Python file using the following code:
2)	Create one or more classes to store and process Product data using the code previous code.
OPTIONAL: If you want to you can create a Blog showing how you accomplished this and
announce it on the discussion forum. However, this is not required!
Step 4: Post your Script
'''

#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input


class product(object):

  def __init__(self, id = "", name = "", price = ""):
    # use properties
    self.id = id
    self.name = name
    self.price = price

    # properties

  # getter or accessor
  @property
  def id(self):
    return self.__id

  # settor or mutator
  @id.setter
  def id(self, value):
    self.__id = value

  # getter or accessor
  @property
  def name(self):
    return self.__name

  # settor or mutator
  @name.setter
  def name(self, value):
    self.__name = value

  # getter or accessor
  @property
  def price(self):
    return self.__price

  # settor or mutator
  @price.setter
  def price(self, value):
    self.__price = value

  def to_string(self):
    return str(self.id) + "," + self.name + "," + str(self.price)

  # override __str__ to call to_string method
  def __str__(self):
    return self.to_string()

  @staticmethod
  def get_lines(prompt="Type in a Product Id, Name, and Price you want to add to the file"):
    # we'll save the entries in a table
    lines=[]
    try:
      print(prompt)
      print("(Enter 'Exit' to quit!)")
      while(True):
        strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
        if(strUserInput.lower() == "exit"): break
        id, name, price = strUserInput.split(",")
        this_product=product(id, name, price)
        lines.append(this_product)
    except:
      print("Unexpected error, please try again.")
    finally:
      return lines

  @staticmethod
  def WriteProductUserInput(File,lines):
    try:
      for line in lines:
        File.write(line.to_string() + "\n")
    except Exception as e:
      print("Error: " + str(e))

  @staticmethod
  def ReadAllFileData(File, Message="Contents of File"):
    try:
      print(Message)
      File.seek(0)
      print(File.read())
    except Exception as e:
      print("Error: " + str(e))

try:
  objFile = open("Products.txt", "r+")
  # read entries into a table
  product.ReadAllFileData(objFile, "Here is the current data:")
  # get new entries
  lines=product.get_lines()
  # if we have any new entries, write them
  if lines:
    product.WriteProductUserInput(objFile,lines)
    product.ReadAllFileData(objFile, "Here is this data was saved:")
  else:
    print("No entries to save.")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()
