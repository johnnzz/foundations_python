# where data in file looks like
# item1,item2
a_list = []
a_file = open("a_file.txt", "r")
for line in a_file:
    print("LINE")
    print(type(line))
    print(line)
    print()
    # read in line of data
    item1, item2 = line.split(",")
    print("ITEMS")
    print(type(item1))
    print(item1)
    print(item2)
    print()
    # create a dict with the items,
    # striping the new line
    dict_entry = { "item1": item1, "item2": item2.strip("\n") }
    print("DICT_ENTRY")
    print(type(dict_entry))
    print(dict_entry)
    print()
    # add dict to a list
    a_list.append(dict_entry)
    print("A_LIST")
    print(type(a_list))
    print(a_list)
    print()
a_file.close()
