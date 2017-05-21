
in_file = open("in.txt", "r")

print("Name of file: ", in_file.name)

for line in in_file:
    print(line)

print(in_file)

in_file.close()
