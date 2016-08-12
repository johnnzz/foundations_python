'''
Module 4 Assignment
Foundations of Programming: Python
13 July 2016

Instructor:  Randal Root
Student:     John Navitsky

Description:

Program loads data from the text file HomeInventory.txt into a 2
dimensional Tuple.  Then asks the user for the name of a household
item, and then asks for its estimated value.  Store them in the 2
dimensional Tuple.  Ask the user, when the program exits, if they
would like to save/add the data to a text file called,
HomeInventory.txt.
'''


# let the user know what we are doing
print()
print("HOME INVENTORY 2000")
print("Add/List the inventory database")

# ensure the inventory file exists to avoid
# a file not found error during read
inventory_file = open("HomeInventory.txt", "a")
inventory_file.close()

# initialize inventory as a tuple
inventory = ()

# read any existing inventory data
inventory_file = open("HomeInventory.txt", "r")
for line in inventory_file:
    # assign item and value from line
    item_name = line.split("|")[0]
    # we don't want the new line from the file
    # as part of the value
    item_value = line.split("|")[1].strip("\n")
    # pack the record into a tuple
    record = (item_name, item_value)
    # add record to the inventory
    inventory = inventory + (record,)
inventory_file.close()

# main entry loop
# ask for entries until user quits
while(True):

    print()
    item_name = input("Enter the name of the item to add, 'exit', or 'list': ")
    # look for an exit request

    # break out of the entry loop when asked
    if item_name.lower() == "exit":
        break

    # show currently loaded items if asked
    if item_name.lower() == "list":
        # don't print header if inventory is empty
        if inventory:
            # give us a header
            print()
            print(" ", "item".ljust(15), "est. value".ljust(10))
            print(" ", "-"*15, "-"*10)
            # print each entry in the inventory
            for record in inventory:
                # unpack the values for processing
                (item_name, item_value) = record
                # print the record
                print(" ", item_name.ljust(15), "$" + str(item_value).ljust(10))
        else:
            print()
            print("  No entries yet")
        # return to input loop
        continue

    # make sure they entered something before adding the entry
    if item_name:

        # try until they enter a numeric value
        while(True):

            # protect against non numeric input
            try:
                item_value = float(input("Enter the estimated value of the " + item_name + ": "))
                # success, got a numeric value so break out of loop
                break

            # caught non numeric input, print msg, try again
            except:
                print("  Item value must be numeric")

        # valid entry, save it

        # pack the record into a tuple
        record = (item_name, item_value)
        # add record to the inventory
        inventory = inventory + (record,)

# don't try to write data if the inventory is empty
if inventory:

    # ask if they'd like to save
    print()
    save_data = input("Would you like to save these records [y/n]? ")

    # save the data
    if save_data.lower() == "y" or save_data.lower() == "yes":

        # open inventory file in write mode in the current directory
        # this overwrites the current file, but we have the previous
        # entries in memory
        inventory_file = open("HomeInventory.txt", "w")

        print()

        # write out the records
        for record in inventory:

            # unpack the values for processing
            (item_name, item_value) = record

            # give the user feedback
            print("...writing: " + item_name)

            # write the entry to the file
            inventory_file.write(item_name + "|" + str(item_value) + "\n")

        # close the file before exiting
        inventory_file.close()

        print()
        print("Inventory updated!")

    else:
        # acknowledge the user decision
        print("OK, next time!")
else:
    # give the user feedback
    print("Goodbye!")