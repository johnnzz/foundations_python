# id name email
# 1 Bob Smith, bsmith@hotmail.com
# 2 Sue Jones, suej@yahoo.com
# 3 Joe James, joejames@gmail.com

# define field descriptions widths
# pad field descriptions to make header printing less complex
field_width = (3, 10, 18)
field_desc = ("id".ljust(field_width[0]), "name".ljust(field_width[1]), "email")

# print the passed customer record
def print_cust():
    informal_name = name.split(" ")[0]
    print()
    print("Here is " + informal_name + "'s record:")
    print()
    # print a header of field descriptions
    for item in field_desc:
        # add a null to match later formatting
        print(item, "", end="")
    print()
    # adjust the field_width to account for spaces between items
    print("-" * (sum(field_width) + 2))

    # print customer, padded to field_width
    print(str(id).ljust(field_width[0]), name.ljust(field_width[1]), email.ljust(field_width[2]))

# load address book
row1 = ( 1, "Bob Smith", "bsmith@hotmail.com")
row2 = ( 2, "Sue Jones", "suej@yahoo.com")
row3 = ( 3, "Joe James", "joejames@gmail.com")
address_book = (row1, row2, row3)

# give user some context
print()
print("Customer Address Database 2000")
print("  search mode")
print()

# search until user quits
while True:
    search_name = input("Enter customer name, 'exit' to exit: ")

    # exit if asked
    if search_name.lower() == "exit":
        break

    # search each record for matching customer
    customer_found = False
    for customer_record in address_book:
        (id, name, email) = customer_record
        if search_name.lower() == name.lower():
            print_cust()
            customer_found = True
    if not customer_found:
        print("Sorry, could not find", search_name, "in the database")
    print()
