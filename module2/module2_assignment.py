'''

Module 2 Assignment
Foundations of Programming: Python
29 June 2016

Instructor:  Randal Root
Student:     John Navitsky

Description:
  Input two numbers then prints sum, difference,
  product and quotient

'''

print("NUMBER TRIVIA")
print()

# try/except block to catch and handle the input
# of non numeric data
try:
  x = float(input(" Enter a number: "))
  y = float(input(" Enter another number: "))    

  print()
  print("Did you know?")

  # add the numbers
  print("", x, "+", y, "=", x+y)
  print("", y, "+", x, "=", y+x)

  # subtract the numbers
  print("", x, "-", y, "=", x-y)
  print("", y, "-", x, "=", y-x)

  # multiply the numbers
  print("", x, "*", y, "=", x*y)
  print("", y, "*", x, "=", y*x)

  # divide the numbers
  
  # protect against divide by zero
  try:
    print("", x, "/", y, "=", x/y)
  except:
    print("", x, "/", y, "=", "undefined")

  # protect against divide by zero
  try:
    print("", y, "/", x, "=", y/x)
  except:
    print("", y, "/", x, "=", "undefined")

  print()
  
except:
  print()
  print("Sorry, your input must be a number.")
  print("Please re-run the program to try again.")
  print()

