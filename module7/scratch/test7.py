
#def afunct():
er1=""
er2=""
q=0
error=""



try:
    x=int("a")
    print("outter try")
    q="1"
    z=1
except Exception as err:
    print("outter except")
    q="2"
    z=2
    error = str(err) + q
    try:
        x=int("bar")
        print("inner try")
        q="3"
        z=3
    except Exception as err:
        x="baz"
        print("inner except")
        q="4"
        z=4
        error=str(err) + q

print("stuff",error)
#print("s2",z)
#print("er1",er1)
#print("er2",er2)