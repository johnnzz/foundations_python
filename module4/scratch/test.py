
item1 = ('mouse', 23.0)
item2 = ('house', 33.0)
item3 = ('cat', 43.0)

# ------


print()

print("thing + ( item1 )")
thing = ()
thing = thing + ( item1 )
print(thing)
thing = thing + ( item2 )
print(thing)

# ------

print("thing + ( item1, )")
thing = ()
thing = thing + ( item1, )
print(thing)
thing = thing + ( item2, )
print(thing)


# ------

inventory_file = open("open-close-test.txt", "a")
inventory_file.write(str(thing))
inventory_file.close()


# ----
print()
thing = ()
thing = thing + ( item1, )
thing = thing + ( item1, )
thing = thing + ( item1, )
thing = thing + ( item1, )
print(thing)
