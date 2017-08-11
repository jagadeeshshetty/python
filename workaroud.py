
varA = 2
varB = 4
name = "name"

if (type(varA) == str or type(varB) == str):
    print("string involved")
elif (type(varA) == int or type(varB) == int):
    print("string did not invlved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")


try:
    2/0
except:
    print("No divide by zero")
    