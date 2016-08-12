
item1 = ('mouse', 23.0)
item2 = ('house', 33.0)
item3 = ('cat', 43.0)
inventory = (item1, item2, item3)

print(inventory)

inventory_file = open("test-data.txt", "w")
inventory_file.write(str(inventory).strip("\n"))
inventory_file.close()

inventory_file = open("test-data.txt", "r")
inventory = inventory_file
inventory_file.close()

print(inventory)
print(type(inventory))


