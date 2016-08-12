'''
1)	Create a function that prints the Sum, Difference, Product, and Quotient of two numbers.
'''

def compute_stuff(x,y):

    values = []
    desc = []

    for item in range(0,8):
        values.append(None)
        desc.append(None)
        #print(item,"prefilling",values[item],desc[item])

    what="sum "
    oper="+"
    desc[0] = what + str(x) + oper + str(y)
    values[0] = x+y
    desc[1] = what + str(y) + oper + str(x)
    values[1] = y+x

    what="difference "
    oper="-"
    desc[2] = what + str(x) + oper + str(y)
    values[2] = x-y
    desc[3] = what + str(y) + oper + str(x)
    values[3] = y-x

    what="product "
    oper="*"
    desc[4] = what + str(x) + oper + str(y)
    values[4] = x*y
    desc[5] = what + str(y) + oper + str(x)
    values[5] = y*x

    what="quotient "
    oper="/"
    desc[6] = what + str(x) + oper + str(y)
    try:
        values[6] = x/y
    except:
        values[6] = False
    desc[7] = what + str(y) + oper + str(x)
    try:
        values[7] = y/x
    except:
        values[7] = False

    return(desc, values)

def print_answer(desc, values):
    for item in range(0,8):
        print( desc[item],"=",values[item] )

while(True):
    try:
        first=input("Enter the first number or [q]uit: ")
        if first in [ "q", "quit", "e", "exit"]:
            print("Goodbye!")
            break
        second=input("Enter the second number: ")
        desc, values=compute_stuff(float(first),float(second))
        print_answer(desc, values)
    except:
        print("  You must enter numbers, try again.")
    print()
