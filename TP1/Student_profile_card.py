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

print("In Py, it does not define that the variable is in a specific type or it's modual")