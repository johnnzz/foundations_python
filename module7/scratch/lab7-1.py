"""
lab7-1
product id, name, price
"""

product_file = open("product.txt","r+")
products=[]

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
