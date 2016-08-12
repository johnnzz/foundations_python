'''
1)	Create a function that prints the Sum, Difference, Product, and Quotient of two numbers.
'''

def compute_stuff(x,y):

    values = {}

    what="sum"
    oper="+"
    values[what,"desc",0] = str(x) + oper + str(y)
    values[what,"val",0] = x+y
    values[what,"desc",1] = str(y) + oper + str(x)
    values[what,"val",1] = y+x

    what="difference"
    oper="-"
    values[what,"desc",0] = str(x) + oper + str(y)
    values[what,"val",0] = x-y
    values[what,"desc",1] = str(y) + oper + str(x)
    values[what,"val",1] = y-x

    what="product"
    oper="*"
    values[what,"desc",0] = str(x) + oper + str(y)
    values[what,"val",0] = x*y
    values[what,"desc",1] = str(y) + oper + str(x)
    values[what,"val",1] = y*x

    what="quotient"
    oper="/"
    values[what,"desc",0] = str(x) + oper + str(y)
    try:
        values[what,"val",0] = x/y
    except:
        values[what,"val",0] = False
    values[what,"desc",1] = str(y) + oper + str(x)
    try:
        values[what,"val",1] = y/x
    except:
        values[what,"val",1] = False

    return(values)

def print_answer(dict):
    for action in ["sum", "difference", "product", "quotient" ]:
        for permutation in [ 0, 1 ]:
            print( dict[(action,"desc",permutation)],"=",dict[(action,"val",permutation)] )

while(True):
    try:
        first=input("Enter the first number or [q]uit: ")
        if first in [ "q", "quit", "e", "exit"]:
            print("Goodbye!")
            break
        second=input("Enter the second number: ")
        answer=compute_stuff(float(first),float(second))
        print_answer(answer)
    except:
        print("  You must enter numbers, try again.")
    print()
