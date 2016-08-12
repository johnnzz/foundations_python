"""
lab3-2
    Write a script that lets a user select one of three options by
    entering an argument when the script starts.
"""
import sys

# Print "Please choose 1, 2, or 3"
def usage():
    print()
    print("You must enter a number between '1' and '3'.")
    print("ex: python lab3-2.py 2")

# ensure the proper number of args have been input
if len(sys.argv) == 2:
    # protect against non numeric input
    try:
        # Get the argument value
        choice = int(sys.argv[1])
        # Print "You chose one" only if option 1 is selected.
        if choice == 1:
            print("You chose one")
        # Print "You chose two" execute only if option 2 is selected.
        elif choice == 2:
            print("You chose two")
        # Print "You chose three" execute only if option 3 is selected.
        elif choice == 3:
            print("You chose three")
        else:
            usage()
    except:
        # non numeric input, print help
        usage()
else:
    # incorrect number of args, print help
    usage()
