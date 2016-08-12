'''
Module 5 Lab 2
Foundations of Programming: Python
21 July 2016

Instructor:  Randal Root
Student:     John Navitsky

Description:

lab05-02
'''


# let the user know what we are doing
print()
print("CUSTOMER DATABASE 2000")
print("Add/List customers")

# ensure the customer file exists to avoid
# a file not found error during read
customer_file = open("customer.txt", "a")
customer_file.close()

# initialize inventory as a list
customer_list = []

# read any existing customer data
customer_file = open("customer.txt", "r")
for line in customer_file:
    # read in line of customer data
    customer_id, customer_name, customer_email = line.split("|")
    # create a list with the customer record stripping the
    # new line from the file
    record = { "id": customer_id, "name": customer_name, "email": customer_email.strip("\n") }
    # add record to the inventory
    customer_list.append(record)
customer_file.close()

# figure out what the last id is
last_id = 1
for record in customer_list:
    if int(record["id"]) > last_id:
        last_id = int(record["id"])

# main entry loop
# ask for entries until user quits
while(True):

    # make sure we start each run without pollution
    customer_id = None
    customer_name = ""
    customer_email = ""

    print()
    customer_name = input("Enter the customer to add, 'exit', or 'list': ")
    # look for an exit request

    # break out of the entry loop when asked
    if customer_name.lower() == "exit":
        break

    # show currently loaded items if asked
    if customer_name.lower() == "list":
        # don't print header if inventory is empty
        if customer_list:
            # give us a header
            print()
            print("id".ljust(4), "name".ljust(20), "email".ljust(20))
            print("-"*4, "-"*20, "-"*20)
            # print each entry in the inventory
            for record in customer_list:
                # print the record
                print(str(record["id"]).ljust(4), record["name"].ljust(20), record["email"].ljust(20))
        else:
            print()
            print("  No entries yet")
        # return to input loop
        continue

    # make sure they entered something before adding the entry
    if customer_name:

        # try until they enter an email:
        while( not customer_email ):
            customer_email = input("Enter " + customer_name + "'s email: ")

        # entry, save it

        # customer id will be the last_id plus 1
        customer_id = last_id + 1
        # increment the last_id
        last_id += 1

        # make a customer record
        record = { "id": customer_id, "name": customer_name, "email": customer_email}

        # add record to the inventory
        customer_list.append(record)

# don't try to write data if the inventory is empty
if customer_list:

    # ask if they'd like to save
    print()
    save_data = input("Would you like to save these records [y/n]? ")

    # save the data
    if save_data.lower() == "y" or save_data.lower() == "yes":

        # open inventory file in write mode in the current directory
        # this overwrites the current file, but we have the previous
        # entries in memory
        customer_file = open("customer.txt", "w")

        print()

        # write out the records
        for record in customer_list:

            # unpack the values for processing
            customer_id = record["id"]
            customer_name = record["name"]
            customer_email = record["email"]

            # give the user feedback
            print("...writing: " + customer_name)

            # write the entry to the file
            customer_file.write(str(customer_id) + "|"+ customer_name + "|" + str(customer_email) + "\n")

        # close the file before exiting
        customer_file.close()

        print()
        print("Customer database updated!")

    else:
        # acknowledge the user decision
        print("OK, next time!")
else:
    # give the user feedback
    print("Goodbye!")