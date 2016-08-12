'''
Module 4 Assignment
Foundations of Programming: Python
13 July 2016

Instructor:  Randal Root
Student:     John Navitsky

Description:

Program that asks the user for the name of a household item, and
then asks for its estimated value.  Ask the user for new entries
and store them in the 2 dimensional Tuple.  Ask the user, when the
program exits, if they would like to save/add the data to a text
file called, HomeInventory.txt.
'''


# let the user know what we are doing
print()
print("HOME INVENTORY 2000")
print("Enter items into the inventory")

# initialize inventory as a tuple
inventory=()

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

        # valid entry, save it

        # pack the record into a tuple
        record = (item_name, item_value)
        # add record to the inventory
        inventory = inventory + (record,)

# don't try to write data if we didn't enter anything
if inventory:

    # ask if they'd like to save
    print()
    print("would you like to save these records?")
    save_data = input("y/n: ")

    # save the data
    if save_data.lower() == "y":

        # open inventory file in append mode in the current directory
        inventory_file = open("HomeInventory.txt", "a")

        print()

        # write out the records
        for record in inventory:

            # unpack the values for processing
            (item_name, item_value) = record

            # give the user feedback
            print("...writing: " + item_name + ", " + str(item_value))

            # write the entry to the file
            inventory_file.write(item_name + "|" + str(item_value) + "\n")

        # close the file before exiting
        inventory_file.close()

        print()
        print("data saved!")

    else:
        # acknowledge the user decision
        print("ok, next time!")
