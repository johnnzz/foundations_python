
# id name email
# 1 Bob Smith, bsmith@hotmail.com
# 2 Sue Jones, suej@yahoo.com
# 3 Joe James, joejames@gmail.com


row_size = (3, 10, 18)
row_desc = ("id".ljust(row_size[0]), "name".ljust(row_size[1]), "email")

row1 = ( 1, "Bob Smith", "bsmith@hotmail.com")
row2 = ( 2, "Sue Jones", "suej@yahoo.com")
row3 = ( 3, "Joe James", "joejames@gmail.com")

address_book = (row1, row2, row3)

for item in row_desc:
    print(item + " ", end="")
print()
print("-" * (sum(row_size)+3) )

for row in address_book:
    #print(row)
    (id, name, email) = row
    print(str(id).ljust(row_size[0]), name.ljust(row_size[1]), email.ljust(row_size[2]))
#        for item in row:
#            print(item)

