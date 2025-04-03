# Walrus Operator

name = input("enter a name: ")

if ((n := len(name)) > 12):
    print(f"Too long {len(name)} elements")

while ((n := len(name)) > 1):
    print(n)
    name = name[:-1]
print(name)
