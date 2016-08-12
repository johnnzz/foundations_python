"""
lab7-2
product id, name, price
"""

file_name = "product.txt"
products=[]

def open_file(file_name):
    product_file=None
    abort=False
    try:
        product_file = open(file_name,"r+")
    except FileNotFoundError as error:
        print("The file, " + file_name + ", doesn't exist.  Please create it and try again!")
        abort=True
    except Exception as error:
        print("The following error has occurred:")
        #print(type(error))
        print(error)
        abort=True
    finally:
        return abort, product_file

def read_file(product_file):
    product_file.seek(0)
    for item in product_file:
        id, product, cost = item.strip("\n").split("|")
        products.append((id,product,cost))
    #return(products)

def print_items(product_file):
    product_file.seek(0)
    for item in product_file:
        id, product, cost = item.strip("\n").split("|")
        print(id,product,cost)

def get_item():
    abort=False
    id=None
    product_name=None
    product_cost=None
    print("enter 'quit' to exit")
    id=input("  enter the id: ")
    if id in [ "exit", "e", "q", "quit" ]:
        abort=True
        return(abort,id,product_name,product_cost)
    product_name=input("  enter the product name: ")
    product_cost=input("  enter the cost: ")
    return(abort,id,product_name,product_cost)

def write_item(product_file,id,product,cost):
    # ensure we are at end of file
    product_file.seek(0, 2)
    product_file.write(id + "|" + product + "|" + cost + "\n")

abort, product_file = open_file(file_name)
if abort:
    print("The program is quiting.")
    exit()

_ = read_file(product_file)
print_items(product_file)

while(True):
    abort,id,product,cost = get_item()
    #print(abort,id,product,cost)
    if not abort:
        #print("let's write it")
        write_item(product_file,id,product,cost)
        continue
    else:
        break

print_items(product_file)
product_file.close()
