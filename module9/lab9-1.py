import DataProcessor

if __name__ != "__main__":
    raise Exception("lab9-1.py is not a module and is intended to be called directly.")

MyFile = DataProcessor.File("data.txt", "save this text")
DataProcessor.File.SaveData(MyFile)
