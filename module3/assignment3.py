'''
Module 3 Assignment
Foundations of Programming: Python
10 July 2016

Instructor:  Randal Root
Student:     John Navitsky

Description:

    Create a program that asks the user for the name of a household
    item, and then asks for its estimated value.  Store, both pieces
    of data in a txt file called, HomeInventory.txt
'''

# open inventory file in append mode in the current directory
inventory_file = open("HomeInventory.txt", "a")

# let the user know what we are doing
print()
print("HOME INVENTORY 2000")
print("Enter items into the inventory")

# ask for entries until user quits
while(True):
    print()
    item_name = input("Enter the name of the item or 'exit' to exit: ")
    # look for an exit request
    if item_name.lower() == "exit":
        break
    # make sure they entered something before proceeding
    if item_name:
        # try until they enter a numeric value
        while(True):
            # protect against non numeric input
            try:
                item_value = float(input("Enter the estimated value of " + item_name + ": "))
                # got a numeric value so break out of loop
                break
            # caught non numeric input, print msg, try again
            except:
                print("  item value must be numeric")
        # valid entry, write data to file in pipe delimited
        # format for easier parsing
        inventory_file.write(item_name + "|" + str(item_value) + "\n")
# close file before exit
inventory_file.close()
