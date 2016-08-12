
item1 = ('mouse', 23.0)
print(type(item1))
print(item1)

print()

item2 = ('house', 33.0)
item3 = ('cat', 43.0)

for element in item1:
  print(element)


# 

row1 = ('mouse', 23.0)
row2 = ('keyboard', 50.0)
sheet = (row1, row2)
print(type(sheet))
print(sheet)




# ------

print("thing + ( item1, )")

thing = ()
item1 = ('mouse', 23.0)
item2 = ('cat', 33.0)

thing = thing + ( item1, )
print(thing)
thing = thing + ( item2, )
print(thing)

print()

print("thing + ( item1 )")


thing = ()
item1 = ('mouse', 23.0)
item2 = ('cat', 33.0)

thing = thing + ( item1 )
print(thing)
thing = thing + ( item2 )
print(thing)

# ------

inventory_file = open("open-close-test.txt", "a")
inventory_file.close()
