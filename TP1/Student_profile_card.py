Name = "Sok Dara"
Age = 20
Major = "Data Sciene"
GPA = 3.67
Scholar = True

# a
print(Name)
print(Age)
print(Major)
print(f"{GPA: .2f}")
print(Scholar)

# b
print(Name,"->",type(Name).__name__)
print(Age,"->",type(Age).__name__)
print(Major,"->",type(Major).__name__)
print(GPA,"->",type(GPA).__name__)
print(Scholar, "->",type(Scholar).__name__)

#c
Age = "20"
print(type(Age))

## What it tells you about dynamic typing: age was an int a moment ago, and now it’s a str, with no error and no type declaration. In Python, the type belongs to the value (the object), not to the variable name. A name is just a label that can be re-pointed at any object, so its type can change while the program runs.