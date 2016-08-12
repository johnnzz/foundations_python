"""
LAB 6-3: Working with classes
1)	Create a class with (4) Methods, have them return a Sum, Difference, Product, and Quotient of two numbers.
2)	Name the class MathProcessor
3)	Name the methods AddValues, SubtractValues, MultiplyValues, DivideValues.
4)	Display the results to the user by calling each method.
"""

class MathProcessor():
    """
    class that does stuff
    """
    @staticmethod

    def AddValues(x,y):
        """
        add values
        """
        return(x+y)

    def SubtractValues(x,y):
        """
        subtract values
        """
        return(x-y)

    def MultiplyValues(x,y):
        """
        multiply values
        """
        return(x*y)

    def DivideValues(x,y):
        """
        divide values
        """
        try:
            value=x/y
        except:
            value="invalid"
        return(value)

while(True):
    try:
        first=input("Enter the first number or [q]uit: ")
        if first in [ "q", "quit", "e", "exit"]:
            print("Goodbye!")
            break
        second=input("Enter the second number: ")

        first = float(first)
        second = float(second)

        print(first,"+",second,"=",MathProcessor.AddValues(first,second))
        print(first,"-",second,"=",MathProcessor.SubtractValues(first,second))
        print(first,"*",second,"=",MathProcessor.MultiplyValues(first,second))
        print(first,"/",second,"=",MathProcessor.DivideValues(first,second))

    except:
        print("  You must enter numbers, try again.")
    print()

