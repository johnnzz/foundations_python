item1 = { "item": "mouse", "value": 23.0 }
print(type(item1))
print(item1)
#---
item1 = { "item": "mouse", "value": 23.0 }
item1["item"] = "cat"
print(item1)
#---
item1 = { "item": "mouse", "value": 23.0 }
print(item1)
print(item1["value"])
item1["status"] = "high"
print(item1)
print(item1["value"])
#---
#a_value = int(input("enter a number: "))
#---
try:
    a_value = int(input("enter a number: "))
except:
    print("only numeric values accepted")
finally:
    print("always do this")