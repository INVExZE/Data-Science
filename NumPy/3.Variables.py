#many values to multiple variables
x="orange"
y="banana"
z="apple"
print(x)
print(y)
print(z)

x, y, z = "orange", "banana", "apple"
print(x)
print(y)
print(z)

x="orange"
y="orange"
z="orange"
print(x)
print(y)
print(z)

x = y = z = "orange"
print(x)
print(y)
print(z)

fruits = ["orange", "banana", "apple"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variable
x = "my name is sanjay"
print(x)

x = "my"
y = "name"
z = "is sanjay"
print(x,y,z)

x = "my "
y = "name "
z = "is sanjay"
print(x + y + z)

x = 5
y = 10
z = 15
print(x + y + z)

#defining global variable
x = "sanjay singh"

def myfuncion():
    print("My name is " + x)

myfuncion()   

#create variable inside a function
def name():
    x = "singh sanjay"
    print("My name is " + x)

name()

print("this is " + x)